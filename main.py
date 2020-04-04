from PyQt5.QtCore import pyqtSlot

import General, PersonOrLocation, Chat, sys, PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,500)
        self.initUI()

    def initUI(self):
        font = QFont()
        font.setPointSize(12)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.te = QTextEdit()
        self.te.setFont(font)
        self.te.setReadOnly(True)
        self.te.append("Heya, how are you? \n > ")
        self.le = QLineEdit()
        self.le.setFont(font)
        self.le.setText("You: ")
        self.le.returnPressed.connect(self.buttonClicked)
        layout = QVBoxLayout()
        layout.addWidget(self.te)
        layout.addWidget(self.le)
        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    def buttonClicked(self):
        self.te.insertPlainText(" "+self.le.text()[5:])
        Chat.Chat(self.le.text()[5:])
        print("here")
        self.te.append(Chat.popStack())
        self.le.setText("You: ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Breeze")
    main = Main()
    sys.exit(app.exec_())


