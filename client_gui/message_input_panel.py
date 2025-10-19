##
# @file message_input_panel.py
# @brief Input box for typing messages.
# @author Oussama Amara
# @date 2025-10-19
# @version 1.0
#Note:
#This widget emits a signal when the user presses Enter.
#You’ll connect this to SendButton or directly to the subprocess later.
##

from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

##
# @class MessageInputPanel
# @brief Provides a text input field for composing messages.
##
class MessageInputPanel(QWidget):
    # Signal emitted when user presses Enter
    message_ready = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Type your message...")
        layout.addWidget(self.input)

        # Emit signal on Enter
        self.input.returnPressed.connect(self.emit_message)

    ##
    # @brief Emits the typed message and clears the input.
    ##
    def emit_message(self):
        text = self.input.text().strip()
        if text:
            self.message_ready.emit(text)
            self.input.clear()
