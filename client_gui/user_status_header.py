##
# @file user_status_header.py
# @brief Top bar showing client ID and connection status.
#        Dynamically updates based on client assignment and server state.
# @author Oussama Amara
# @date 2025-10-26
# @version 1.3
##

from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout

##
# @class UserStatusHeader
# @brief Displays current client ID and connection status.
##
class UserStatusHeader(QWidget):
   
    def __init__(self):
        super().__init__()

        self.setFixedHeight(30)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        self.setLayout(layout)

        self.username_label = QLabel("👤 Unknown")
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

    ##
    # @brief Updates the displayed client ID.
    # @param client_id Assigned client ID from server.
    ##
    def set_client_id(self, client_id: str):
        self.username_label.setText(f"👤 Client #{client_id}")
