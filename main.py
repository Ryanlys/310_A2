from PyQt5.QtCore import*

import General, PersonOrLocation, Chat, sys, PyQt5, sentiment, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

negativePlace = ["Aw, that's too bad. ", "That sucks to hear, ", "Oof, "]
negativePerson = ["That doesn't sound good. ", "Aw, ", "Hmm,"]
positivePlace = ["That's good to hear, ", "I'll definitely check it out, ", "Cool, "]
positivePerson = ["Aw,","That's sweet, "]

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,500)
        self.initUI()
        sentiment.train()

    def initUI(self):
        font = QFont()
        font.setPointSize(12)
        font.setFamily("Rockwell")
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.te = QTextEdit()
        self.te.setFont(font)
        self.te.setReadOnly(True)
        self.te.append("Heya, how are you? \n >")
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
        if General.getLastSentence()=="":
            Chat.Chat(self.le.text()[5:])
            self.te.setAlignment(Qt.AlignLeft)
            self.te.append(Chat.popStack())
        else:
            print(General.getLastSentence())
            if (len(General.getLastSentence().split("!!")) != 1):
                if (General.getLastSentence().split("!!")[1] == "place"):
                    if sentiment.classify(self.le.text()[5:]) == "Negative":
                        out = negativePlace[random.randint(0,len(negativePlace)-1)]
                        Chat.Chat(self.le.text()[5:])
                        self.te.append(out+Chat.popStack().lower())
                    else:
                        out = positivePlace[random.randint(0, len(positivePlace) - 1)]
                        Chat.Chat(self.le.text()[5:])
                        self.te.append(out + Chat.popStack().lower())
                elif sentiment.classify(self.le.text()[5:]) == "Negative":
                    out = negativePerson[random.randint(0, len(negativePerson) - 1)]
                    Chat.Chat(self.le.text()[5:])
                    self.te.append(out + Chat.popStack().lower())
                else:
                    out = positivePerson[random.randint(0, len(positivePerson) - 1)]
                    Chat.Chat(self.le.text()[5:])
                    self.te.append(out + Chat.popStack().lower())
            else:
                Chat.Chat(self.le.text()[5:])
                self.te.append(Chat.popStack())
        self.le.setText("You: ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Breeze")
    main = Main()
    sys.exit(app.exec_())


