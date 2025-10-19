##
# @file chat_history_panel.py
# @brief Scrollable panel showing message history.
# @author Oussama Amara
# @date 2025-10-19
# @version 1.0
#Note:
#This panel shows all messages in a scrollable view.
#You’ll call append_message() when a new frame is received.
##

from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout

##
# @class ChatHistoryPanel
# @brief Displays incoming and outgoing messages.
##
class ChatHistoryPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.history = QTextEdit()
        self.history.setReadOnly(True)
        layout.addWidget(self.history)

    ##
    # @brief Appends a message to the history view.
    # @param sender Sender name or ID.
    # @param message Message content.
    ##
    def append_message(self, sender, message):
        self.history.append(f"<b>{sender}:</b> {message}")
