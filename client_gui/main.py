##
# @file main.py
# @brief Entry point for the PyQt5 GUI client of Server_Client-C-app.
#        Sets up the main window layout and loads placeholder panels.
#        This GUI wraps the compiled C client binary (subprocess integration comes later).
# @author Oussama
# @date 2025-10-19
# @version 1.0
##

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QStatusBar
)
from PyQt5.QtCore import Qt

# Import placeholder panels (we'll define these next)
from conversation_list_panel import ConversationListPanel
from user_status_header import UserStatusHeader
from window_control_panel import WindowControlPanel
from chat_history_panel import ChatHistoryPanel
from message_input_panel import MessageInputPanel
from send_button import SendButton

##
# @class MainWindow
# @brief Main application window that hosts all GUI components.
##
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Server_Client-C-app GUI")
        self.setMinimumSize(1000, 700)

        # Create central widget and layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # ─── Top Bar: User Status + Window Controls ─────────────────────────────
        top_bar = QHBoxLayout()
        self.user_status = UserStatusHeader()
        self.window_controls = WindowControlPanel()
        top_bar.addWidget(self.user_status)
        top_bar.addStretch()
        top_bar.addWidget(self.window_controls)
        main_layout.addLayout(top_bar)

        # ─── Middle Section: Sidebar + Chat Panel ───────────────────────────────
        middle_splitter = QSplitter(Qt.Horizontal)

        # Sidebar: Conversation list
        self.sidebar = ConversationListPanel()
        middle_splitter.addWidget(self.sidebar)

        # Chat panel: History + Input
        chat_panel = QWidget()
        chat_layout = QVBoxLayout()
        chat_panel.setLayout(chat_layout)

        self.chat_history = ChatHistoryPanel()
        self.message_input = MessageInputPanel()
        self.send_button = SendButton()

        chat_layout.addWidget(self.chat_history)
        chat_layout.addWidget(self.message_input)
        chat_layout.addWidget(self.send_button)

        middle_splitter.addWidget(chat_panel)
        middle_splitter.setStretchFactor(1, 1)
        main_layout.addWidget(middle_splitter)

        # ─── Status Bar ─────────────────────────────────────────────────────────
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Disconnected")

##
# @brief Initializes the Qt application and launches the main window.
##
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# Entry point
if __name__ == "__main__":
    main()
