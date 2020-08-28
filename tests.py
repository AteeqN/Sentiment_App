import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        #create bar
        bar = self.menuBar()

        #create bar menus
        file = bar.addMenu("File")
        about = bar.addMenu("About")

        #create actions
        quit_action = QAction("&Quit", self)
        quit_action.setShortcut('Ctrl+Q')
        about_action = QAction("&About...", self)

        #add actions
        file.addAction(quit_action)
        about.addAction(about_action)

        #what to do with actions
        quit_action.triggered.connect(self.quit_func)
        about_action.triggered.connect(self.about_func)

        #window properties
        self.setWindowTitle("Hello World")
        self.resize(600, 400)

        self.show()

    def quit_func(self):
        sys.exit()

    def about_func(self):
        pass

class About(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #widgets
        self.l1 = QLabel('Hello World')
        self.l1.setAlignment(Qt.AlignCenter)
        self.l2 = QLabel('Description of the Application')
        self.l2.setAlignment(Qt.AlignCenter)

        #horiz box
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l2)
        h_box.addStretch()

        #vert box
        v_box = QVBoxLayout()
        v_box.addWidget(self.l1)
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.setLayout(v_box)

        #window properties
        self.setWindowTitle("About Hello World")
        self.setFixedSize(250,150)

        self.show()

if not QApplication.instance():
    app = QApplication(sys.argv)
else:
    app = QApplication.instance()

main = Menu()
abt = About()
main.show()
abt.show()

sys.exit(app.exec())