##
# @file main.py
# @brief Entry point for the PyQt5 GUI client of Server_Client-C-app.
#        Launches the C client with config, monitors stdout, and updates GUI status and identity.
# @author Oussama
# @date 2025-10-26
# @version 1.4
##

import sys
import subprocess
import os
import platform
import threading
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
# @brief Main application window that hosts all GUI components and launches the C client.
##
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ─── Window Setup ──────────────────────────────────────────────────────
        self.setWindowTitle("Server_Client-C-app GUI")
        self.setMinimumSize(600, 400)
        self.client_process = None
        self.client_id = None

        # ─── Central Layout ─────────────────────────────────────────────────────
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # ─── Top Bar: User Status ───────────────────────────────────────────────
        top_bar = QHBoxLayout()
        top_bar.setContentsMargins(0, 0, 0, 0)
        top_bar.setSpacing(5)
        top_bar.addStretch()
        self.user_status = UserStatusHeader()
        top_bar.addWidget(self.user_status)
        main_layout.addLayout(top_bar)

        # ─── Middle Section: Sidebar + Chat Panel ───────────────────────────────
        middle_splitter = QSplitter(Qt.Horizontal)

        self.sidebar = ConversationListPanel()
        middle_splitter.addWidget(self.sidebar)

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

        # ─── Launch C Client ────────────────────────────────────────────────────
        self.launch_client()

        # ─── Signal Wiring ──────────────────────────────────────────────────────
        self.message_input.message_ready.connect(self.handle_message)

    ##
    # @brief Launches the compiled C client with the chat config file.
    ##
    def launch_client(self):
        is_windows = platform.system() == "Windows"
        binary_name = "client.exe" if is_windows else "client"
        client_path = os.path.abspath(binary_name)
        config_path = os.path.abspath("assets/client_chat.cfg")

        if not os.path.exists(client_path):
            self.status.showMessage("Client binary not found.")
            return

        try:
            self.client_process = subprocess.Popen(
                [client_path, config_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            threading.Thread(target=self.monitor_client_output, daemon=True).start()
            self.status.showMessage("Client launched.")
        except Exception as e:
            self.status.showMessage(f"Failed to launch client: {e}")

    ##
    # @brief Monitors client stdout for connection status and assigned ID.
    ##
    def monitor_client_output(self):
        for line in self.client_process.stdout:
            print("[CLIENT]", line.strip())

            if "Assigned client ID:" in line:
                try:
                    self.client_id = line.strip().split(":")[1].strip()
                    self.user_status.set_client_id(self.client_id)
                except Exception:
                    pass

            elif "Connection failed" in line:
                self.status.showMessage("⚪❌ Problem connecting to the server")
                self.user_status.set_connected(False)

            elif "Connected to server" in line:
                self.status.showMessage("🟢 Connected to server")
                self.user_status.set_connected(True)

            elif "Waiting for another client" in line:
                self.status.showMessage("⏳ Waiting for another client...")

    ##
    # @brief Handles message dispatch from input panel.
    # @param text Message content.
    ##
    def handle_message(self, text):
        sender = f"Client #{self.client_id}" if self.client_id else "You"
        self.chat_history.append_message(sender, text)
        # TODO: Forward message to C client subprocess when integrated

    ##
    # @brief Ensures client subprocess is terminated on exit.
    ##
    def closeEvent(self, event):
        if self.client_process:
            self.client_process.terminate()
        event.accept()

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
