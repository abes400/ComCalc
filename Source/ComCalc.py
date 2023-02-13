from sys import argv
from os.path import expanduser
from Functions import initFolder, initRoll, initSettings
from WindowManager import StartApp

if __name__ == "__main__":
    initFolder()
    initRoll()
    initSettings()

    file = open(expanduser('~') + '/ComCalc/settings.inf', 'r')
    filelist = file.read().split()
    file.close()

    StartApp(argv, filelist)
