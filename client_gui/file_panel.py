##
# @file file_panel.py
# @brief File transfer panel with file picker and progress display.
##

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QProgressBar
from PyQt5.QtCore import pyqtSignal

##
# @class FilePanel
# @brief Panel for sending files and tracking progress.
##
class FilePanel(QWidget):
    # Signal emitted when a file is selected for sending
    file_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # File picker button
        self.pick_btn = QPushButton("Select File")
        layout.addWidget(self.pick_btn)

        # File name label
        self.file_label = QLabel("No file selected")
        layout.addWidget(self.file_label)

        # Progress bar
        self.progress = QProgressBar()
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        # Connect button
        self.pick_btn.clicked.connect(self.select_file)

    ##
    # @brief Opens file dialog and emits selected file path.
    ##
    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if path:
            self.file_label.setText(path)
            self.file_selected.emit(path)

    ##
    # @brief Updates progress bar.
    # @param percent Completion percentage.
    ##
    def update_progress(self, percent):
        self.progress.setValue(percent)

