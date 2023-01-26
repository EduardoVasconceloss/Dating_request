from ui_main import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtCore import QEvent
import random

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.coracao.setVisible(False)

        self.button_no.clicked.connect(self.moveButton)
        self.frame_no.installEventFilter(self)


    def moveButton(self):
        self.frame_no.move(random.randint(0, 300), random.randint(0, 300))
    

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter and obj == self.frame_no:
            self.moveButton()
            return True
        else:
            return False
        

app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.exec()