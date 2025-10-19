##
# @file sidebar.py
# @brief Sidebar navigation widget for the GUI client.
#        Mimics Microsoft Teams layout with icons for Chat, Files, and Settings.
#        Emits signals to switch main content panels.
# @author Oussama
# @date 2025-10-19
# @version 1.0
##

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon

##
# @class Sidebar
# @brief Sidebar widget with navigation items and signal for panel switching.
##
class Sidebar(QWidget):
    # Signal emitted when a panel is selected (e.g., "chat", "files")
    switch_panel = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Navigation list
        self.nav_list = QListWidget()
        self.nav_list.setSpacing(5)
        self.nav_list.setStyleSheet("QListWidget { border: none; }")

        # Add navigation items
        self.add_nav_item("Chat", "chat", "assets/icons/chat.png")
        self.add_nav_item("Files", "files", "assets/icons/files.png")
        self.add_nav_item("Settings", "settings", "assets/icons/settings.png")

        # Connect selection signal
        self.nav_list.currentItemChanged.connect(self.on_item_selected)

        layout.addWidget(self.nav_list)
        self.setLayout(layout)

    ##
    # @brief Adds a navigation item to the sidebar.
    # @param label Display name of the item.
    # @param panel_key Internal key used to switch panels.
    # @param icon_path Path to the icon file.
    ##
    def add_nav_item(self, label, panel_key, icon_path):
        item = QListWidgetItem(QIcon(icon_path), label)
        item.setData(Qt.UserRole, panel_key)
        self.nav_list.addItem(item)

    ##
    # @brief Handles item selection and emits panel switch signal.
    # @param current The currently selected QListWidgetItem.
    # @param previous The previously selected QListWidgetItem.
    ##
    def on_item_selected(self, current, previous):
        if current:
            panel_key = current.data(Qt.UserRole)
            self.switch_panel.emit(panel_key)
