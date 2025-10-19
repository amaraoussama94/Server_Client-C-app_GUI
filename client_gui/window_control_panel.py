##
# @file window_control_panel.py
# @brief Custom window control buttons (minimize, maximize, close).
# @author Oussama Amara
# @date 2025-10-19
# @version 1.0
#Note:
#These buttons are placeholders for window control.
#You can later connect them to self.parent().showMinimized() etc.
##

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

##
# @class WindowControlPanel
# @brief Provides standard window control buttons.
##
class WindowControlPanel(QWidget):
    
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        # Minimize button
        self.min_btn = QPushButton("—")
        self.max_btn = QPushButton("□")
        self.close_btn = QPushButton("✕")

        layout.addWidget(self.min_btn)
        layout.addWidget(self.max_btn)
        layout.addWidget(self.close_btn)

        # Connect buttons to window actions (to be wired in main.py)
