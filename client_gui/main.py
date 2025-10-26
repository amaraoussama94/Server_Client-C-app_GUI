##
# @file main.py
# @brief Entry point for the PyQt5 GUI client of Server_Client-C-app.
#        Sets up the main window layout and loads placeholder panels.
#        This GUI wraps the compiled C client binary (subprocess integration comes later).
#        Currently uses native OS window frame; frameless mode planned.
# @author Oussama
# @date 2025-10-26
# @version 1.1
##

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QStatusBar
)
from PyQt5.QtCore import Qt

from conversation_list_panel import ConversationListPanel
from user_status_header import UserStatusHeader
from chat_history_panel import ChatHistoryPanel
from message_input_panel import MessageInputPanel

##
# @class MainWindow
# @brief Main application window that hosts all GUI components.
##
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ─── Window Setup ──────────────────────────────────────────────────────
        self.setWindowTitle("Server_Client-C-app GUI")
        self.setMinimumSize(600, 400)

        # TODO: In future, enable frameless mode with:
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # Then implement drag-to-move and custom window controls

        # ─── Central Layout ─────────────────────────────────────────────────────
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # ─── Top Bar: User Status ───────────────────────────────────────────────
        top_bar = QHBoxLayout()
        top_bar.addStretch() 
        self.user_status = UserStatusHeader()
        top_bar.addWidget(self.user_status)
        #top_bar.addStretch()
        #. Remove Extra Padding in
        top_bar.setContentsMargins(0, 0, 0, 0)
        top_bar.setSpacing(5)

        main_layout.addLayout(top_bar)

        # ─── Middle Section: Sidebar + Chat Panel ───────────────────────────────
        middle_splitter = QSplitter(Qt.Horizontal)

        self.sidebar = ConversationListPanel()
        middle_splitter.addWidget(self.sidebar)
        middle_splitter.setStretchFactor(0, 0)
        chat_panel = QWidget()
        chat_layout = QVBoxLayout()
        chat_panel.setLayout(chat_layout)

        self.chat_history = ChatHistoryPanel()
        self.message_input = MessageInputPanel()

        chat_layout.addWidget(self.chat_history)
        chat_layout.addWidget(self.message_input)

        middle_splitter.addWidget(chat_panel)
        middle_splitter.setStretchFactor(1, 1)
        main_layout.addWidget(middle_splitter)

        # ─── Status Bar ─────────────────────────────────────────────────────────
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Disconnected")

        # ─── Signal Wiring ──────────────────────────────────────────────────────
        self.message_input.message_ready.connect(self.handle_message)

    ##
    # @brief Handles message dispatch from input panel.
    # @param text Message content.
    ##
    def handle_message(self, text):
        self.chat_history.append_message("You", text)
        # TODO: Forward message to C client subprocess when integrated

##
# @brief Initializes the Qt application and launches the main window.
##
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
