##
# @file conversation_list_panel.py
# @brief Sidebar panel listing all conversations (clients or groups).
#
# @author Oussama
# @date 2025-10-19
# @version 1.0
##
#Note:
#This panel uses QListWidget to show a vertical list of clients or groups.
#Later, you can connect selection events to load the corresponding chat history.
##

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel

##
# @class ConversationListPanel
# @brief Displays a vertical list of conversations for selection.
##
class ConversationListPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title label
        title = QLabel("Conversations")
        layout.addWidget(title)

        # List of conversations (dummy for now)
        self.list_widget = QListWidget()
        self.list_widget.addItems([
            "Client #1",
            "Client #2",
            "Group: Dev Team",
            "Client #3"
        ])
        layout.addWidget(self.list_widget)
