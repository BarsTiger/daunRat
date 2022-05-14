import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from data.settings import Settings
sys.path.append('gui')

try:
    from gui import Ui_MainWindow
except ImportError:
    from gui.gui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def openMenu():
    width = ui.leftMenu.geometry().width()
    Ui_MainWindow.animation = QtCore.QPropertyAnimation(ui.leftMenu, b"minimumWidth")
    Ui_MainWindow.animation.setDuration(Settings.animation()["timing"])
    if width == 60:
        Ui_MainWindow.animation.setStartValue(60)
        Ui_MainWindow.animation.setEndValue(200)
    else:
        Ui_MainWindow.animation.setStartValue(200)
        Ui_MainWindow.animation.setEndValue(60)
    Ui_MainWindow.animation.setEasingCurve(Settings.animation()["animation"])

    Ui_MainWindow.animation.start()


def handleMenuClick(text):
    match text:
        case "Menu":
            openMenu()
        case "Devices":
            ui.pagesWidget.setCurrentIndex(0)
        case "Screenshot":
            ui.pagesWidget.setCurrentIndex(1)
        case "Wallpaper":
            ui.pagesWidget.setCurrentIndex(2)


ui.leftMenu.itemClicked.connect(lambda: handleMenuClick(ui.leftMenu.currentItem().text()))

sys.exit(app.exec_())
