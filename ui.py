from PyQt6.QtWidgets import QApplication,QWidget,QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,300)
        self.move(300,300)
        self.setWindowTitle('first app')
        self.setup_ui()
    def setup_ui(self):
        label = QLabel(self)
        label.setText('This is my first app')
        label.move(100,100)

if __name__ =='__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())