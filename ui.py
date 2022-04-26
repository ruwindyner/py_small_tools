from cProfile import label
from PyQt6.QtWidgets import QApplication,QWidget,QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('the first app')
        self.resize(500,500)
        self.move(200,245)
        self.setup_ui()
    def setup_ui(self):
        label = QLabel(self)
        label.setText('this is my first app')
        label.move(200,245)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
