import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle('Main application window')
        self.resize(500, 400)

        self.status = self.statusBar()
        self.status.showMessage('This is the status bar and the message only exists 5 seconds')

        self.button = QPushButton('Close the window')
        self.button.clicked.connect(self.click)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        MainFrame = QWidget()
        MainFrame.setLayout(layout)
        self.setCentralWidget(MainFrame)


    def click(self):
        sender = self.sender()
        print(sender.text()+' 按钮被按下')
        app = QApplication.instance()
        app.quit()



if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())