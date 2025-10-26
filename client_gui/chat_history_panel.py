##
# @file chat_history_panel.py
# @brief Scrollable panel showing message history.
#        Automatically scrolls to latest message.
# @author Oussama Amara
# @date 2025-10-26
# @version 1.1
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
        self.history.moveCursor(self.history.textCursor().End)
