import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from Functions import error
from os.path import expanduser

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.rollenabled = 0
        self.dotadded = False
        self.opradded = False

        # Define Layout
        self.setWindowTitle("")
        self.vert = qtw.QVBoxLayout()
        self.hor = qtw.QHBoxLayout()
        self.gri = qtw.QGridLayout()
        self.miniver = qtw.QVBoxLayout()

        # Prepare the Layout
        self.vert.addLayout(self.hor)
        self.gri.addLayout(self.miniver, 2, 4)
        self.vert.addLayout(self.gri)
        self.setLayout(self.vert)
        
        self.gri.setVerticalSpacing(3)
        self.gri.setHorizontalSpacing(3)
        self.layout().setContentsMargins(8, 8, 8, 8)

        # Screen object shows entered digit(s) and operation results
        self.screen = qtw.QLineEdit(self, readOnly = True)
        self.screen.setStyleSheet('background-color: #FFFFFF')
        self.screen.setText('0')
        self.screen.setFont(qtg.QFont('Avenir', 30))
        self.screen.setAlignment(qtc.Qt.AlignRight)

        #Number Keys
        self.key7 = qtw.QPushButton('\n7\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '7')))
        self.key8 = qtw.QPushButton('\n8\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '8')))
        self.key9 = qtw.QPushButton('\n9\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '9')))
        self.key4 = qtw.QPushButton('\n4\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '4')))
        self.key5 = qtw.QPushButton('\n5\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '5')))
        self.key6 = qtw.QPushButton('\n6\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '6')))
        self.key1 = qtw.QPushButton('\n1\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '1')))
        self.key2 = qtw.QPushButton('\n2\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '2')))
        self.key3 = qtw.QPushButton('\n3\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '3')))
        self.key0 = qtw.QPushButton('\n0\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '0')))
        self.keyD = qtw.QPushButton('\n•\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '.')))

        self.key7.setShortcut('7')
        self.key8.setShortcut('8')
        self.key9.setShortcut('9')
        self.key4.setShortcut('4')
        self.key5.setShortcut('5')
        self.key6.setShortcut('6')
        self.key1.setShortcut('1')
        self.key2.setShortcut('2')
        self.key3.setShortcut('3')
        self.key0.setShortcut('0')
        self.keyD.setShortcut('.')

        #Operational Keys
        self.divKey = qtw.QPushButton('', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '/')))
        self.mulKey = qtw.QPushButton('', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '*')))
        self.subKey = qtw.QPushButton('\n－\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '-')))
        self.addKey = qtw.QPushButton('\n＋\n', clicked = lambda: self.screen.setText(self.scrapd(self.screen.text(), '+')))

        # Shortcuts of the operational keys are defined at Functions.py

        #Extra Keys
        self.clrKey = qtw.QPushButton('\nC\n', clicked=lambda: self.screen.setText(self.resetcalc()))
        self.delKey = qtw.QPushButton('\n⌫\n', clicked=lambda: self.screen.setText(self.backspace(self.screen.text())))
        self.equKey = qtw.QPushButton('\n=\n', clicked=lambda: self.screen.setText(self.equals(self.screen.text())))

        self.clrKey.setShortcut('C')
        self.equKey.setShortcut('Return')

        # Adding the widgets to the window
        self.hor.addWidget(self.screen)
        self.gri.addWidget(self.key7, 0, 0)
        self.gri.addWidget(self.key8, 0, 1)
        self.gri.addWidget(self.key9, 0, 2)
        self.gri.addWidget(self.key4, 1, 0)
        self.gri.addWidget(self.key5, 1, 1)
        self.gri.addWidget(self.key6, 1, 2)
        self.gri.addWidget(self.key1, 2, 0)
        self.gri.addWidget(self.key2, 2, 1)
        self.gri.addWidget(self.key3, 2, 2)
        self.gri.addWidget(self.key0, 3, 0, 1, 2)
        self.gri.addWidget(self.keyD, 3, 2)
        self.gri.addWidget(self.divKey, 0, 3)
        self.gri.addWidget(self.mulKey, 1, 3)
        self.gri.addWidget(self.subKey, 2, 3)
        self.gri.addWidget(self.addKey, 3, 3)
        self.gri.addWidget(self.clrKey, 1, 4)
        self.gri.addWidget(self.delKey, 0, 4)
        self.gri.addWidget(self.equKey, 3, 4)

        self.show()
    
    # The functions assigned to the buttons are defined below
    
    # Appends the value of the button to the content of the screen
    def scrapd(self, onScreenContent, appendedValue):
        if len(onScreenContent) == 16:
            return onScreenContent
        if appendedValue == '.' and not self.dotadded:
            self.dotadded = True
            return onScreenContent + '.'
        elif appendedValue == '.' and self.dotadded:
            return onScreenContent
        elif onScreenContent == '0' or onScreenContent == '0.0':
            if appendedValue == '*' or appendedValue == '/':
                self.opradded = True
                return '0' + appendedValue
            elif appendedValue == '+' or appendedValue == '-':
                self.opradded = True
                return appendedValue
            else:
                return appendedValue
        elif appendedValue == '+' or appendedValue == '-' or appendedValue == '*' or appendedValue == '/':
            if not self.opradded:
                if onScreenContent[-1] == '.':
                    onScreenContent += '0'
                self.dotadded = False
                self.opradded = True
                return onScreenContent + appendedValue
            else:
                return onScreenContent
        else:
            self.opradded = False
            return onScreenContent + appendedValue

    # Evaluates the content of the screen
    def equals(self, onScreenContent):
        self.dotadded = False
        self.dotadded = True
        try:
            if onScreenContent[-1] == '+' or onScreenContent[-1] == '-':
                result = eval(onScreenContent + '0.0')
                self.writeToRoll(onScreenContent + '=' +str(result))
                return str(result)
            elif onScreenContent[-1] == '*' or onScreenContent[-1] == '/':
                result = eval(onScreenContent + '1.0')
                self.writeToRoll(onScreenContent + '=' +str(result))
                return str(result)
            else:
                result = eval(onScreenContent) + 0.0
                self.writeToRoll(onScreenContent + '=' +str(result))
                return str(result)
        except Exception as e:
            self.writeToRoll(onScreenContent + '=Undefined')
            error(1)
            return '0'

    # If enabled from the options, writes the operaton to the abstract file called paper_roll.txt
    def writeToRoll(self, eqn):
        if self.rollenabled:
            self.rollfile = open(expanduser('~') + '/ComCalc/paper_roll.txt', 'a')
            self.rollfile.write(eqn + '\n')
            self.rollfile.close()

    # Removes the last character of the content of the screen
    def backspace(self, onScreenContent):
        try:
            if onScreenContent[-1] == '+' or onScreenContent[-1] == '-'\
            or onScreenContent[-1] == '*' or onScreenContent[-1] == '/':
                self.opradded = False
            elif onScreenContent[-1] == '.':
                self.dotadded = False
            if len(onScreenContent) == 1:
                return '0'
            onScreenContent = onScreenContent.removesuffix(onScreenContent[-1])
            return onScreenContent
        except Exception as e:
            return '0'
    
    # Resets the calculator to its initial state
    def resetcalc(self):
        self.opradded = False
        self.dotadded = False
        return '0'

    def closeEvent(self, event):
        self.deleteLater()
