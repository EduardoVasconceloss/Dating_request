from PySide6 import QtWidgets
from PySide6.QtCore import QEvent

from ui_main import Ui_MainWindow

import random


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.heart.setVisible(False)

        self.no_button.clicked.connect(self.moveButton)
        self.yes_button.clicked.connect(self.bestOption)

        self.no_frame.installEventFilter(self)
        self.yes_frame.installEventFilter(self)

    def moveButton(self):
        self.no_frame.move(random.randint(0, 300), random.randint(0, 300))

    def bestOption(self):
        self.question.setText("You chose the best option!!!")
        self.question.setStyleSheet("QLabel{\n"
                                    "	font-size: 30px;\n"
                                    "	font-weight: bold;\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "}\n")
        self.yes_button.setVisible(False)
        self.no_button.setVisible(False)
        self.heart.setVisible(True)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter and obj == self.no_frame:
            self.moveButton()
            return True
        else:
            return False


app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.exec()
