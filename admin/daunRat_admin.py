# Imports
import sys
from PyQt5 import QtWidgets, QtCore
from data.settings import Settings
import pusher
import pusher.errors
import pysher
import modules.exception as exception
sys.path.append('gui')
# Importing the main window
try:
    from gui import Ui_MainWindow
    from functions import *
except ImportError:
    from gui.gui import Ui_MainWindow
    from gui.functions import *

# Hooking exceptions
sys.excepthook = exception.hook

# Getting config
settings = Settings.get_settings()

# Global variables for annotations
client = pusher.Pusher
receiver = pysher.Pusher

# Initializing the main window
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.pagesWidget.setCurrentIndex(0)

# Trying to get settings or set default
try:
    fill_settings(ui)
except Exception as e:
    print(e)
    Settings.fix()

# Creating gui
MainWindow.show()


def initialize_pusher() -> None:
    """
    Registers the pusher client and receiver
    :return:
    """
    global client
    global receiver
    client = pusher.Pusher(
        app_id=settings["app_id"],
        key=settings["key"],
        secret=settings["secret"],
        cluster=settings["cluster"],
        ssl=False
    )
    receiver = pysher.Pusher(key=settings["key"], cluster=settings["cluster"])
    receiver.connection.bind('pusher:connection_established', handle_connection_to_server)
    receiver.connect()


def open_menu() -> None:
    """
    Animates the menu to open and close, using animation from config
    :return:
    """
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


def handle_menu_click(text: str) -> None:
    """
    Handles the click on the menu and changes the page
    :param text:
    :return:
    """
    match text:
        case "Menu":
            open_menu()
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


def handle_connection_to_server(connection) -> None:
    """
    On pusher connection
    :return:
    """
    print("Connected to server")
    print("Server returned: " + str(connection))
    try:
        for client_id_av in list(client.channels_info(prefix_filter='admin-')['channels']):
            print("Channel: " + client_id_av.split('-')[1])
    except pusher.errors.PusherBadRequest:
        popup("Error", "Could not connect to pusher server\n"
                       "Do you have valid pusher config in settings tab?")


def reconnect_to_pusher() -> None:
    """
    Reconnects to pusher
    :return:
    """
    global receiver
    receiver.disconnect()
    print("Disconnected from pusher")
    initialize_pusher()


# Trying to connect to pusher
initialize_pusher()

# Connecting user interface to functions
ui.leftMenu.itemClicked.connect(lambda: handle_menu_click(ui.leftMenu.currentItem().text()))
ui.saveSettingsButton.clicked.connect(lambda: (globals().update(settings=update_settings(ui))))
ui.reconRefreshButton.clicked.connect(lambda: reconnect_to_pusher())

# Handling closing of the window to exit whole program
sys.exit(app.exec_())
