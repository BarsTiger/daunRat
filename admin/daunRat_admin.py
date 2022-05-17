import sys
from PyQt5 import QtWidgets, QtCore
from data.settings import Settings
sys.path.append('gui')

try:
    from gui import Ui_MainWindow
    from functions import *
except ImportError:
    from gui.gui import Ui_MainWindow
    from gui.functions import *

settings = Settings.get_settings()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

try:
    fill_settings(ui)
except Exception as e:
    print(e)
    Settings.fix()

MainWindow.show()


def openMenu() -> None:
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


def handleMenuClick(text: str) -> None:
    match text:
        case "Menu":
            openMenu()
        case "Devices":
            ui.pagesWidget.setCurrentIndex(1)
        case "Screenshot":
            ui.pagesWidget.setCurrentIndex(2)
        case "Wallpaper":
            ui.pagesWidget.setCurrentIndex(3)
        case "Console":
            ui.pagesWidget.setCurrentIndex(4)
        case "Python":
            ui.pagesWidget.setCurrentIndex(5)
        case "Download":
            ui.pagesWidget.setCurrentIndex(6)
        case "Settings":
            ui.pagesWidget.setCurrentIndex(7)


ui.leftMenu.itemClicked.connect(lambda: handleMenuClick(ui.leftMenu.currentItem().text()))
ui.saveSettingsButton.clicked.connect(lambda: update_settings(ui))

sys.exit(app.exec_())
