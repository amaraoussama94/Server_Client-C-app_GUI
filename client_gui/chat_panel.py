##
# @file chat_panel.py
# @brief Chat interface panel with message history and input box.
#        Supports sending messages and displaying incoming ones.
##

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import pyqtSignal

##
# @class ChatPanel
# @brief Panel for chat messaging with input and display.
##
class ChatPanel(QWidget):
    # Signal emitted when a message is sent
    message_sent = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # Layouts
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Message history display
        self.history = QTextEdit()
        self.history.setReadOnly(True)
        layout.addWidget(self.history)

        # Input box and send button
        input_layout = QHBoxLayout()
        self.input = QLineEdit()
        self.send_btn = QPushButton("Send")
        input_layout.addWidget(self.input)
        input_layout.addWidget(self.send_btn)
        layout.addLayout(input_layout)

        # Connect send button
        self.send_btn.clicked.connect(self.send_message)

    ##
    # @brief Emits message and clears input box.
    ##
    def send_message(self):
        text = self.input.text().strip()
        if text:
            self.message_sent.emit(text)
            self.input.clear()

    ##
    # @brief Appends a message to the history view.
    # @param sender Name or ID of the sender.
    # @param message Message content.
    ##
    def append_message(self, sender, message):
        self.history.append(f"<b>{sender}:</b> {message}")
