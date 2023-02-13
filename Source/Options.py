from os.path import expanduser
import PyQt5.QtWidgets as qtw
from Functions import changeth, error

class Setup(qtw.QDialog):
    def __init__(self, app, window):
        super().__init__()

        self.setWindowTitle("Options")
        self.setFixedSize(245, 130)
        self.setModal(True)

        self.gri = qtw.QGridLayout()
        self.gri2 = qtw.QGridLayout()
        self.gri3 = qtw.QGridLayout()
        self.ver = qtw.QVBoxLayout()
        self.ver.addLayout(self.gri)
        self.ver.addLayout(self.gri3)
        self.ver.addLayout(self.gri2)
        self.setLayout(self.ver)

        self.file = open(expanduser('~') + '/ComCalc/settings.inf', 'r')
        self.filelist = self.file.read().split()
        self.file.close()

        self.themes = qtw.QComboBox(self)
        self.themes.addItem("Fusion", 0)
        self.themes.addItem("Windowsill", 1)
        self.themes.setCurrentIndex(int(self.filelist[0]))

        self.color = qtw.QComboBox(self)
        self.color.addItem("Red", 1)
        self.color.addItem("Orange", 2)
        self.color.addItem("Yellow", 3)
        self.color.addItem("Green", 4)
        self.color.addItem("Blue", 5)
        self.color.addItem("Purple", 6)
        self.color.addItem("Black", 7)
        self.color.addItem("White", 8)
        self.color.setCurrentIndex(int(self.filelist[1])-1)

        self.rollset = qtw.QCheckBox('Enable Paper Roll')
        self.rollset.setChecked(int(self.filelist[2]))

        self.short = qtw.QPushButton('Shortcuts', clicked = lambda: error(2))
        self.applykey = qtw.QPushButton('✓ Apply', clicked=lambda: self.apply(app, window))
        self.infokey = qtw.QPushButton('ⓘ About', clicked=lambda: error(4))
        self.closekey = qtw.QPushButton('✗ Discard', clicked=lambda: self.close())

        self.gri.addWidget(qtw.QLabel('Theme'), 0, 0)
        self.gri.addWidget(self.themes, 0, 1, 1, 3)
        self.gri.addWidget(qtw.QLabel('Color'), 1, 0)
        self.gri.addWidget(self.color, 1, 1, 1, 3)
        self.gri3.addWidget(self.rollset, 0, 0)
        self.gri2.addWidget(self.applykey, 2, 1)
        self.gri3.addWidget(self.short, 0, 1)
        self.gri2.addWidget(self.infokey, 2, 0)
        self.gri2.addWidget(self.closekey, 2, 2)

        self.show()

    def apply(self, app, window):
        file2 = open(expanduser('~') + '/ComCalc/settings.inf', 'w')
        file2.write(str(self.themes.currentIndex()) + ' ' + str(self.color.currentData())
                    + ' ' + str(int(self.rollset.isChecked())))
        file2.close()

        changeth(self.color.currentData(), self.themes.currentIndex(),
                 int(self.rollset.isChecked()), app, window)

        self.close()

    def closeEvent(self, event):
        self.deleteLater()
