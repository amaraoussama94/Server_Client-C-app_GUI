##
# @file send_button.py
# @brief Button to send message or trigger file transfer.
# @author Oussama Amara
# @date 2025-10-19
# @version 1.0
#Note:
#This button emits a signal when clicked.
#You’ll connect it to the subprocess wrapper to send the frame.
##

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

##
# @class SendButton
# @brief Action button to confirm sending message or file.
##
class SendButton(QWidget):

    # Signal emitted when button is clicked
    send_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button = QPushButton("Send")
        layout.addWidget(self.button)

        self.button.clicked.connect(self.send_clicked.emit)
