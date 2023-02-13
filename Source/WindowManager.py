from MainWindow import MainWindow
from Options import Setup
from PaperRollView import PaperRoll
from Functions import changeth, initSettings
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

def RunSetup(app, CalcWindow):
    Setup(app, CalcWindow)

def ViewRoll():
    PaperRoll()

def StartApp(arg, filelist):
    app = qtw.QApplication(arg)
    CalcWindow = MainWindow()

    CalcWindow.infKey = qtw.QPushButton('ᵒᵖᵗˢ', clicked=lambda: RunSetup(app, CalcWindow))
    CalcWindow.infKey.setFont(qtg.QFont('Arial', 20))
    CalcWindow.infKey.setShortcut('Ctrl+O')
    CalcWindow.miniver.addWidget(CalcWindow.infKey)

    CalcWindow.rollKey = qtw.QPushButton('ʳᵒˡˡ', clicked= lambda: ViewRoll())
    CalcWindow.rollKey.setFont(qtg.QFont('Arial', 20))
    CalcWindow.rollKey.setShortcut('Ctrl+R')
    CalcWindow.miniver.addWidget(CalcWindow.rollKey)

    try:
       changeth(int(filelist[1]), int(filelist[0]), int(filelist[2]), app, CalcWindow)

    except Exception as e:
        initSettings(1)
        changeth(5, 0, 1, app, CalcWindow)

    exit(app.exec_())
