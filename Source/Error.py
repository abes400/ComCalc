import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class Error(qtw.QDialog):
    def __init__(self, x):
        super().__init__()
        self.setWindowTitle("")
        self.setModal(True)

        self.gri = qtw.QGridLayout()
        self.ver = qtw.QVBoxLayout()
        self.ver2 = qtw.QVBoxLayout()
        self.ver.addLayout(self.ver2)
        self.ver.addLayout(self.gri)
        self.setLayout(self.ver)

        if x == 1:
            self.setWindowTitle('Invalid Operation')
            self.ver2.addWidget(qtw.QLabel("     The operation you have entered\n     is invalid."))
            self.setFixedSize(250, 100)

        if x == 2:
            self.setWindowTitle('Keyboard Shortcuts')
            self.ver2.addWidget(qtw.QLabel("     ⌘O    Show options\n     ⌘R    Show paper roll\n"
                                           "     C      C key on calculator"))
            self.setFixedSize(250, 100)

        elif x == 4:
            self.setWindowTitle('About')
            title1 = qtw.QLabel("Compact Calculator (ComCalc)")
            credit = qtw.QLabel("Version 2.0")
            credit2 = qtw.QLabel("KNOWN BUGS:\n     - Unwanted ability to add multiple dots (.)"
                                 "\n     - Being unable to negate an element"
                                 "\n     after adding another operation")

            title1.setFont(qtg.QFont('Arial', 15))
            title1.setAlignment(qtc.Qt.AlignCenter)
            credit.setFont(qtg.QFont('Arial', 10))
            credit.setAlignment(qtc.Qt.AlignCenter)
            credit2.setFont(qtg.QFont('Arial', 10))

            self.setFixedSize(250, 150)
            self.ver2.addWidget(title1)
            self.ver2.addWidget(credit)
            self.ver2.addWidget(credit2)

        self.dismisskey = qtw.QPushButton("✗  Dismiss", clicked = lambda: self.close())

        self.gri.addWidget(qtw.QLabel(' '), 0, 0)
        self.gri.addWidget(qtw.QLabel(' '), 0, 1)
        self.gri.addWidget(self.dismisskey, 0, 2)

        self.show()

    def closeEvent(self, event):
        self.deleteLater()
