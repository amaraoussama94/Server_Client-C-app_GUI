##
# @file main.py
# @brief Entry point for the PyQt5 GUI client of Server_Client-C-app.
#        Initializes the main window, sidebar navigation, and core panels.
#        Mimics Microsoft Teams layout with modular design.
# @author Oussama Amara
# @date 2025-10-19
# @version 1.0
##

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QSplitter, QStatusBar
)
from PyQt5.QtCore import Qt

# Import modular panels
from sidebar import Sidebar         # Sidebar navigation (Chat, Files, Settings)
from chat_panel import ChatPanel    # Chat interface
from file_panel import FilePanel    # File transfer interface

##
# @class MainWindow
# @brief Main application window that hosts sidebar and dynamic content panels.
##
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Server_Client-C-app GUI")
        self.setMinimumSize(900, 600)

        # Create central widget and layout
        central_widget = QWidget()
        central_layout = QHBoxLayout()
        central_widget.setLayout(central_layout)

        # Initialize sidebar (Teams-style navigation)
        self.sidebar = Sidebar()
        self.sidebar.setFixedWidth(200)

        # Initialize main content panels
        self.chat_panel = ChatPanel()
        self.file_panel = FilePanel()

        # Use QSplitter to separate sidebar and main panel
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.sidebar)
        self.splitter.addWidget(self.chat_panel)  # Default view
        self.splitter.setStretchFactor(1, 1)

        # Add splitter to layout
        central_layout.addWidget(self.splitter)
        self.setCentralWidget(central_widget)

        # Add status bar for connection/log messages
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Disconnected")

        # Connect sidebar signal to panel switcher
        self.sidebar.switch_panel.connect(self.load_panel)

    ##
    # @brief Switches the main panel based on sidebar selection.
    # @param panel_name Name of the panel to load ("chat", "files", etc.)
    ##
    def load_panel(self, panel_name):
        # Remove current panel
        self.splitter.widget(1).deleteLater()

        # Insert selected panel
        if panel_name == "chat":
            self.splitter.insertWidget(1, self.chat_panel)
        elif panel_name == "files":
            self.splitter.insertWidget(1, self.file_panel)
        # Future panels (e.g., settings) can be added here

##
# @brief Initializes the Qt application and launches the main window.
##
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# Entry point
if __name__ == "__main__":
    main()
