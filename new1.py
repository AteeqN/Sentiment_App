import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.button = QtWidgets.QPushButton("test", self)
        self.label = QtWidgets.QLabel("console output")
        self.textedit = QtWidgets.QTextEdit(readOnly=True)

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        layout.addWidget(self.textedit)
        self.setCentralWidget(widget)

        self.process = QtCore.QProcess()
        self.process.setProgram(sys.executable)
        self.process.readyReadStandardError.connect(self.on_readyReadStandardError)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)

        self.button.clicked.connect(self.on_clicked)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        self.process.setWorkingDirectory(CURRENT_DIR)
        self.process.setArguments(["-m", "pytest", "-s", "-k", "test_something"])
        self.process.start()

    @QtCore.pyqtSlot()
    def on_readyReadStandardError(self):
        err = self.process.readAllStandardError().data().decode()
        self.textedit.append(err)


    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        out = self.process.readAllStandardOutput().data().decode()
        self.textedit.append(out)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())