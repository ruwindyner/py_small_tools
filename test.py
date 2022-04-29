from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget
from pyqt.Ui_demo import *
from set16its import Escape_data


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)



    def generate(self):
        str1 = self.textEdit.toPlainText()
        str2 = Escape_data(str(str1))
        print(str2)
        self.textEdit.clear()
        self.textEdit_2.setPlainText(str2)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())