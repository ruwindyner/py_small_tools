import sys
from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QMainWindow
from pyqt.Ui_firstmainwin import *


class myMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(myMainWindow,self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = myMainWindow()
    mywin.show()
    sys.exit(app.exec())