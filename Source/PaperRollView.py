from os.path import expanduser
import PyQt5.QtWidgets as qtw

class PaperRoll(qtw.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Paper Roll View')
        self.setFixedSize(280, 280)
        self.setModal(True)

        self.gri = qtw.QGridLayout()
        self.vert = qtw.QVBoxLayout()
        self.hor = qtw.QHBoxLayout()
        self.vert.addLayout(self.hor)
        self.vert.addLayout(self.gri)
        self.setLayout(self.vert)

        self.delroll = qtw.QPushButton('⌫ Clear', clicked = lambda: self.clearRoll())
        self.closeroll = qtw.QPushButton('✗ Dismiss', clicked = lambda: self.close())
        self.RollContent = qtw.QTextEdit(readOnly = True)

        self.file = open(expanduser('~') + '/ComCalc/paper_roll.txt', 'r')
        self.RollContent.setText(self.file.read())
        self.file.close()

        self.hor.addWidget(self.RollContent)
        self.gri.addWidget(qtw.QLabel(''), 0, 0)
        self.gri.addWidget(self.closeroll, 0, 4)
        self.gri.addWidget(self.delroll, 0, 3)

        self.show()

    def clearRoll(self):
        self.file = open(expanduser('~') + '/ComCalc/paper_roll.txt', 'w')
        self.file.close()
        self.RollContent.setText('')

    def closeEvent(self, event):
        self.deleteLater()
