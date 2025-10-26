##
# @file user_status_header.py
# @brief Top bar showing username, avatar, and connection status.
# @author Oussama Amara
# @date 2025-10-19
# @version 1.0
#Note:
#This widget shows your username and connection status.
#Later, you can update status_label dynamically when the client connects.
##

from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout

##
# @class UserStatusHeader
# @brief Displays current user info and connection status.
##
class UserStatusHeader(QWidget):
   
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        # Username label
        self.username_label = QLabel("👤 Oussama")
        layout.addWidget(self.username_label)
        self.setFixedHeight(30)  # Or try 25 for tighter layout
        # Connection status
        self.status_label = QLabel("🔴 Disconnected")
        layout.addWidget(self.status_label)
        self.username_label.setStyleSheet("font-size: 12px; padding: 0px;")
        self.status_label.setStyleSheet("font-size: 12px; padding: 0px;")

