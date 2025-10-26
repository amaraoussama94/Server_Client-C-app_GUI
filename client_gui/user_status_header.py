##
# @file user_status_header.py
# @brief Top bar showing username and connection status.
#        Supports multiple status icons including server error.
# @author Oussama Amara
# @date 2025-10-26
# @version 1.2
##

from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout

##
# @class UserStatusHeader
# @brief Displays current user info and connection status.
##
class UserStatusHeader(QWidget):
   
    def __init__(self):
        super().__init__()

        self.setFixedHeight(30)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        self.setLayout(layout)

        self.username_label = QLabel("👤 Oussama")
        self.username_label.setStyleSheet("font-size: 12px; padding: 0px;")

        self.status_label = QLabel("🔴 Disconnected")
        self.status_label.setStyleSheet("font-size: 12px; padding: 0px;")

        layout.addWidget(self.username_label)
        layout.addWidget(self.status_label)

    ##
    # @brief Updates the connection status indicator.
    # @param connected True if connected, False if server unreachable.
    ##
    def set_connected(self, connected: bool):
        if connected:
            self.status_label.setText("🟢 Connected")
        else:
            self.status_label.setText("⚪❌ Problem connecting to the server")
