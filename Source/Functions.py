from os.path import expanduser, exists
from os import mkdir
from Error import Error
import PyQt5.QtGui as qtg

def changeth(x, y, z, app, window):
    #The list where the accent colors are defined. The accent colors are used in the keys other than numeric ones
    # [a, b]
    # a: color of the divKey, mulKey, subKey, addKey, clrKey, delKey, infKey and optKey objects
    # b: background color, foreground color and label size of the equKey (Without font size, the equals mark will be smaller.)
    themelist = [['background-color: #E49878', 'background-color: #D80000; color: white; font-size: 19px'],
                 ['background-color: #FECE96', 'background-color: #FF8A00; color: white; font-size: 19px'],
                 ['background-color: #FDEB9D', 'background-color: #FFD100; color: black; font-size: 19px'],
                 ['background-color: #AAC8AD', 'background-color: #008E12; color: white; font-size: 19px'],
                 ['background-color: #93AAC0', 'background-color: #1D70BC; color: white; font-size: 19px'],
                 ['background-color: #E9ABFF', 'background-color: #BC00FF; color: white; font-size: 19px'],
                 ['background-color: #989696', 'background-color: #343333; color: white; font-size: 19px'],
                 ['background-color: #FFFFFF', 'background-color: #DCDCDC; color: black; font-size: 19px'],]

    # The list where the theme of the MainWindow object is defined.
    # [a, b, c, d, e, f, g, h]
    # a: Theme name on PyQt5
    # b: The color of the MainWindow class, label size of the QPushButton objects, BG color of QPushButton objects for numeric key
    # c: Font family used in the MainWindow class (button labels and screen),
    # d: Font size used in the screen object
    # e: Width and height of the MainWindow object
    # f: Label used on the mulKey object
    # g: Label used on the divKey object
    # g: Label used on the delKey object
    stylelist = [
        ['Fusion', 'background-color: #F6F7F6; QPushButton{font-size: 15px;'
         'background-color: #ffffff};','Avenir' ,30, 280, '\n✗\n', '\n÷\n', '\n⌫\n'],
        ['Windows', 'background-color: #EBEBEB; QPushButton{font-size: 5px;'
         'background-color: #ffffff};','Arial' ,20, 260, '\n*\n', '\n/\n', '\nback\n']]

    # Setting the color of the button objects
    window.divKey.setStyleSheet(themelist[x - 1][0])
    window.mulKey.setStyleSheet(themelist[x - 1][0])
    window.subKey.setStyleSheet(themelist[x - 1][0])
    window.addKey.setStyleSheet(themelist[x - 1][0])
    window.delKey.setStyleSheet(themelist[x - 1][0])
    window.clrKey.setStyleSheet(themelist[x - 1][0])
    window.infKey.setStyleSheet(themelist[x - 1][0])
    window.rollKey.setStyleSheet(themelist[x - 1][0])
    window.equKey.setStyleSheet(themelist[x - 1][1])

    # Setting the theme of the window objects
    app.setStyle(stylelist[y][0])
    window.setStyleSheet(stylelist[y][1])
    window.screen.setFont(qtg.QFont(stylelist[y][2], stylelist[y][3]))
    window.setFixedSize(stylelist[y][4], stylelist[y][4])
    window.mulKey.setText(stylelist[y][5])
    window.divKey.setText(stylelist[y][6])
    window.delKey.setText(stylelist[y][7])

    # As mentioned in the MainWindow.py file, the operand keys are defined here since somehow, PyQt5 keeps resetting
    # the shortcut assigned to the buttons whenever their labels are c changed.
    window.subKey.setShortcut('-')
    window.addKey.setShortcut('+')
    window.divKey.setShortcut('/')
    window.mulKey.setShortcut('*')
    window.delKey.setShortcut('BackSpace')

    # Changes the roll setting of the MainWindow object
    window.rollenabled = z

def initFolder():
    if not exists(expanduser('~') + '/ComCalc'):
        mkdir(expanduser('~') + '/ComCalc')

def initSettings(dontCheckCondition = 0):
    if dontCheckCondition or not exists(expanduser('~') + '/ComCalc/settings.inf'):
        file = open(expanduser('~') + '/ComCalc/settings.inf', 'w')
        file.write('0 5 1')
        file.close()

def initRoll():
    if not exists(expanduser('~') + '/ComCalc/paper_roll.txt'):
        file = open(expanduser('~') + '/ComCalc/paper_roll.txt', 'w')
        file.close()

def error(x):
    Error(x)
