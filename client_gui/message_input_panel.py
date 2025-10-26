##
# @file message_input_panel.py
# @brief Input box for typing messages, with embedded send button.
#        Emits signal when user presses Enter or clicks Send.
# @author Oussama Amara
# @date 2025-10-26
# @version 1.1
##

from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import pyqtSignal

##
# @class MessageInputPanel
# @brief Provides a text input field and send button for composing messages.
##
class MessageInputPanel(QWidget):
    message_ready = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Type your message...")
        self.send_button = QPushButton("Send")

        layout.addWidget(self.input)
        layout.addWidget(self.send_button)

        self.input.returnPressed.connect(self.emit_message)
        self.send_button.clicked.connect(self.emit_message)

    ##
    # @brief Emits the typed message and clears the input.
    ##
    def emit_message(self):
        text = self.input.text().strip()
        if text:
            self.message_ready.emit(text)
            self.input.clear()
