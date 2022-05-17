# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(36)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 380))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"QWidget {\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical,\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(30, 30, 30);\n"
"    width: 10px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {    \n"
"    background-color: rgb(139, 139, 139);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover,\n"
"QScrollBar::handle:vertical:pressed,\n"
"QScrollBar::handle:horizontal:hover,\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"    background-color: rgb(149, 149, 149);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical, \n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-style: solid;\n"
"    border-color: #303030;\n"
"    background-color: #2c2d2e;\n"
"}\n"
"QPushButton:hover {\n"
"    border-width: 2px;\n"
"    background-color: #323232;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #262728;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #434343;\n"
"    border-color: #0000;\n"
"}\n"
"\n"
"\n"
"QLineEdit, QTextBrowser, QPlainTextEdit, QTextEdit {\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-color: #303030;\n"
"    background-color: #242424;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"QListWidget {\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-color: #303030;\n"
"    padding: 10px;\n"
"    background-color: #242424;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QListWidget:item {\n"
"    background-color: #242424;\n"
"    selection-color: white;\n"
"}\n"
"QListWidget:item:hover {\n"
"    background-color: #323232;\n"
"}\n"
"QListWidget:item:selected {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-style: solid;\n"
"    border-color: #303030;\n"
"    background-color: #2c2d2e;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"    background-color: #434343;\n"
"    color: #656565;\n"
"    border-color: #434343;\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #434343;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #434343;\n"
"    color: #ffffff;\n"
"    selection-background-color: #777777;\n"
"    selection-color: white;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    border-radius: 6px; \n"
"}\n"
"\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background-color: #2c2d2e;\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-color: #303030;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"}\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"    background-color: #a0a0a0;\n"
"    color: #ffffff;\n"
"    border: 3px solid;\n"
"    border-radius: 15px;\n"
"    border-color: #1c1c1c;\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: #262728;\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-color: #303030;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected:disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"}\n"
"\n"
"QTabBar::tab:!selected \n"
"{\n"
"    background-color: #262626;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover \n"
"{\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected \n"
"{\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected \n"
"{\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom \n"
"{\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected \n"
"{\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected \n"
"{\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one \n"
"{\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected \n"
"{\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right \n"
"{\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected \n"
"{\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected \n"
"{\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one \n"
"{\n"
"    margin-bottom: 0;\n"
"}\n"
"")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QtWidgets.QListWidget(self.centralwidget)
        self.leftMenu.setMinimumSize(QtCore.QSize(60, 0))
        self.leftMenu.setMaximumSize(QtCore.QSize(60, 16777215))
        self.leftMenu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leftMenu.setStyleSheet("QListWidget {\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    background-color: #242424;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QListWidget:item {\n"
"    padding-left: 10px;\n"
"    height: 60px;\n"
"    background-color: #191919;\n"
"    selection-color: rgba(255, 255, 255);\n"
"}\n"
"QListWidget:item:hover {\n"
"    background-color: #323232;\n"
"}\n"
"QListWidget:item:selected {\n"
"    background-color: #262728;\n"
"}")
        self.leftMenu.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftMenu.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftMenu.setAutoScroll(False)
        self.leftMenu.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.leftMenu.setTabKeyNavigation(False)
        self.leftMenu.setProperty("showDropIndicator", False)
        self.leftMenu.setIconSize(QtCore.QSize(30, 30))
        self.leftMenu.setTextElideMode(QtCore.Qt.ElideRight)
        self.leftMenu.setResizeMode(QtWidgets.QListView.Fixed)
        self.leftMenu.setObjectName("leftMenu")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.leftMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/devices.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.leftMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/screenshot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.leftMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/wallpaper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.leftMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/cmd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.leftMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.leftMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon7)
        self.leftMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon8)
        self.leftMenu.addItem(item)
        self.horizontalLayout.addWidget(self.leftMenu)
        self.pagesWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pagesWidget.sizePolicy().hasHeightForWidth())
        self.pagesWidget.setSizePolicy(sizePolicy)
        self.pagesWidget.setObjectName("pagesWidget")
        self.startPage = QtWidgets.QWidget()
        self.startPage.setObjectName("startPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.startPage)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dLogo = QtWidgets.QLabel(self.startPage)
        self.dLogo.setStyleSheet("font: 166pt \"Comic Sans MS\";\n"
"color: rgb(40, 40, 40);")
        self.dLogo.setObjectName("dLogo")
        self.verticalLayout_6.addWidget(self.dLogo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.choosePanelLabel = QtWidgets.QLabel(self.startPage)
        self.choosePanelLabel.setStyleSheet("color: rgb(70, 70, 70);")
        self.choosePanelLabel.setObjectName("choosePanelLabel")
        self.verticalLayout_6.addWidget(self.choosePanelLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pagesWidget.addWidget(self.startPage)
        self.devicesPage = QtWidgets.QWidget()
        self.devicesPage.setObjectName("devicesPage")
        self.devicesButtonLayout = QtWidgets.QVBoxLayout(self.devicesPage)
        self.devicesButtonLayout.setObjectName("devicesButtonLayout")
        self.availableDevices = QtWidgets.QListWidget(self.devicesPage)
        self.availableDevices.setFocusPolicy(QtCore.Qt.TabFocus)
        self.availableDevices.setObjectName("availableDevices")
        self.devicesButtonLayout.addWidget(self.availableDevices)
        self.devicesButtonsLayout = QtWidgets.QHBoxLayout()
        self.devicesButtonsLayout.setSpacing(6)
        self.devicesButtonsLayout.setObjectName("devicesButtonsLayout")
        self.connectButton = QtWidgets.QPushButton(self.devicesPage)
        self.connectButton.setMinimumSize(QtCore.QSize(0, 30))
        self.connectButton.setObjectName("connectButton")
        self.devicesButtonsLayout.addWidget(self.connectButton)
        self.pingButton = QtWidgets.QPushButton(self.devicesPage)
        self.pingButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pingButton.setObjectName("pingButton")
        self.devicesButtonsLayout.addWidget(self.pingButton)
        self.reconRefreshButton = QtWidgets.QPushButton(self.devicesPage)
        self.reconRefreshButton.setMinimumSize(QtCore.QSize(0, 30))
        self.reconRefreshButton.setObjectName("reconRefreshButton")
        self.devicesButtonsLayout.addWidget(self.reconRefreshButton)
        self.devicesButtonLayout.addLayout(self.devicesButtonsLayout)
        self.pagesWidget.addWidget(self.devicesPage)
        self.screenshotPage = QtWidgets.QWidget()
        self.screenshotPage.setObjectName("screenshotPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.screenshotPage)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.screenshotLayout = QtWidgets.QWidget(self.screenshotPage)
        self.screenshotLayout.setObjectName("screenshotLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.screenshotLayout)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.screenshotLabel = QtWidgets.QLabel(self.screenshotLayout)
        self.screenshotLabel.setText("")
        self.screenshotLabel.setPixmap(QtGui.QPixmap(":/img/img/screen-template.png"))
        self.screenshotLabel.setScaledContents(True)
        self.screenshotLabel.setObjectName("screenshotLabel")
        self.verticalLayout.addWidget(self.screenshotLabel)
        self.takeScreenshotButton = QtWidgets.QPushButton(self.screenshotLayout)
        self.takeScreenshotButton.setStyleSheet("QPushButton {\n"
"    border-radius: 0px;\n"
"}")
        self.takeScreenshotButton.setObjectName("takeScreenshotButton")
        self.verticalLayout.addWidget(self.takeScreenshotButton)
        self.gridLayout_2.addWidget(self.screenshotLayout, 0, 0, 1, 1)
        self.pagesWidget.addWidget(self.screenshotPage)
        self.wallpaperPage = QtWidgets.QWidget()
        self.wallpaperPage.setObjectName("wallpaperPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wallpaperPage)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wallpaperSetLayout = QtWidgets.QWidget(self.wallpaperPage)
        self.wallpaperSetLayout.setObjectName("wallpaperSetLayout")
        self.wallpaperSetterLayout = QtWidgets.QHBoxLayout(self.wallpaperSetLayout)
        self.wallpaperSetterLayout.setObjectName("wallpaperSetterLayout")
        self.wallpaperUrlBox = QtWidgets.QLineEdit(self.wallpaperSetLayout)
        self.wallpaperUrlBox.setMinimumSize(QtCore.QSize(0, 30))
        self.wallpaperUrlBox.setObjectName("wallpaperUrlBox")
        self.wallpaperSetterLayout.addWidget(self.wallpaperUrlBox)
        self.setWallpaperButton = QtWidgets.QPushButton(self.wallpaperSetLayout)
        self.setWallpaperButton.setMinimumSize(QtCore.QSize(100, 30))
        self.setWallpaperButton.setObjectName("setWallpaperButton")
        self.wallpaperSetterLayout.addWidget(self.setWallpaperButton)
        self.verticalLayout_3.addWidget(self.wallpaperSetLayout, 0, QtCore.Qt.AlignTop)
        self.wallpaperEngineControlLayout = QtWidgets.QWidget(self.wallpaperPage)
        self.wallpaperEngineControlLayout.setObjectName("wallpaperEngineControlLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wallpaperEngineControlLayout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.controlWallpaperEngineLabel = QtWidgets.QLabel(self.wallpaperEngineControlLayout)
        self.controlWallpaperEngineLabel.setObjectName("controlWallpaperEngineLabel")
        self.verticalLayout_2.addWidget(self.controlWallpaperEngineLabel, 0, QtCore.Qt.AlignHCenter)
        self.wallpaperEngineControlHorizontalLayout = QtWidgets.QWidget(self.wallpaperEngineControlLayout)
        self.wallpaperEngineControlHorizontalLayout.setObjectName("wallpaperEngineControlHorizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wallpaperEngineControlHorizontalLayout)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stopWallpaperEngineButton = QtWidgets.QPushButton(self.wallpaperEngineControlHorizontalLayout)
        self.stopWallpaperEngineButton.setMinimumSize(QtCore.QSize(0, 30))
        self.stopWallpaperEngineButton.setObjectName("stopWallpaperEngineButton")
        self.horizontalLayout_2.addWidget(self.stopWallpaperEngineButton)
        self.pauseWallpaperEngineButton = QtWidgets.QPushButton(self.wallpaperEngineControlHorizontalLayout)
        self.pauseWallpaperEngineButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pauseWallpaperEngineButton.setObjectName("pauseWallpaperEngineButton")
        self.horizontalLayout_2.addWidget(self.pauseWallpaperEngineButton)
        self.playWallpaperEngineButton = QtWidgets.QPushButton(self.wallpaperEngineControlHorizontalLayout)
        self.playWallpaperEngineButton.setMinimumSize(QtCore.QSize(0, 30))
        self.playWallpaperEngineButton.setObjectName("playWallpaperEngineButton")
        self.horizontalLayout_2.addWidget(self.playWallpaperEngineButton)
        self.muteWallpaperEngineButton = QtWidgets.QPushButton(self.wallpaperEngineControlHorizontalLayout)
        self.muteWallpaperEngineButton.setMinimumSize(QtCore.QSize(0, 30))
        self.muteWallpaperEngineButton.setObjectName("muteWallpaperEngineButton")
        self.horizontalLayout_2.addWidget(self.muteWallpaperEngineButton)
        self.unmuteWallpaperEngineButton = QtWidgets.QPushButton(self.wallpaperEngineControlHorizontalLayout)
        self.unmuteWallpaperEngineButton.setMinimumSize(QtCore.QSize(0, 30))
        self.unmuteWallpaperEngineButton.setObjectName("unmuteWallpaperEngineButton")
        self.horizontalLayout_2.addWidget(self.unmuteWallpaperEngineButton)
        self.verticalLayout_2.addWidget(self.wallpaperEngineControlHorizontalLayout, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.wallpaperEngineControlLayout, 0, QtCore.Qt.AlignTop)
        self.wallpaperScreenshotButton = QtWidgets.QPushButton(self.wallpaperPage)
        self.wallpaperScreenshotButton.setMinimumSize(QtCore.QSize(300, 30))
        self.wallpaperScreenshotButton.setMaximumSize(QtCore.QSize(300, 16777215))
        self.wallpaperScreenshotButton.setObjectName("wallpaperScreenshotButton")
        self.verticalLayout_3.addWidget(self.wallpaperScreenshotButton, 0, QtCore.Qt.AlignHCenter)
        self.wallpaperLogs = QtWidgets.QTextBrowser(self.wallpaperPage)
        self.wallpaperLogs.setObjectName("wallpaperLogs")
        self.verticalLayout_3.addWidget(self.wallpaperLogs)
        self.daunApWallpaperLabel = QtWidgets.QLabel(self.wallpaperPage)
        self.daunApWallpaperLabel.setObjectName("daunApWallpaperLabel")
        self.verticalLayout_3.addWidget(self.daunApWallpaperLabel)
        self.pagesWidget.addWidget(self.wallpaperPage)
        self.consolePage = QtWidgets.QWidget()
        self.consolePage.setObjectName("consolePage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.consolePage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sendCommandLayout = QtWidgets.QWidget(self.consolePage)
        self.sendCommandLayout.setObjectName("sendCommandLayout")
        self.wallpaperSetterLayout_2 = QtWidgets.QHBoxLayout(self.sendCommandLayout)
        self.wallpaperSetterLayout_2.setObjectName("wallpaperSetterLayout_2")
        self.commandBox = QtWidgets.QLineEdit(self.sendCommandLayout)
        self.commandBox.setMinimumSize(QtCore.QSize(0, 30))
        self.commandBox.setObjectName("commandBox")
        self.wallpaperSetterLayout_2.addWidget(self.commandBox)
        self.sendCommandButton = QtWidgets.QPushButton(self.sendCommandLayout)
        self.sendCommandButton.setMinimumSize(QtCore.QSize(100, 30))
        self.sendCommandButton.setObjectName("sendCommandButton")
        self.wallpaperSetterLayout_2.addWidget(self.sendCommandButton)
        self.verticalLayout_4.addWidget(self.sendCommandLayout)
        self.logsConsole = QtWidgets.QTextBrowser(self.consolePage)
        self.logsConsole.setObjectName("logsConsole")
        self.verticalLayout_4.addWidget(self.logsConsole)
        self.clearConsoleLogs = QtWidgets.QPushButton(self.consolePage)
        self.clearConsoleLogs.setMinimumSize(QtCore.QSize(0, 30))
        self.clearConsoleLogs.setObjectName("clearConsoleLogs")
        self.verticalLayout_4.addWidget(self.clearConsoleLogs)
        self.pagesWidget.addWidget(self.consolePage)
        self.pythonPage = QtWidgets.QWidget()
        self.pythonPage.setObjectName("pythonPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pythonPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pythonEditWigdet = QtWidgets.QWidget(self.pythonPage)
        self.pythonEditWigdet.setObjectName("pythonEditWigdet")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.pythonEditWigdet)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pythonScriptEditor = QtWidgets.QTextEdit(self.pythonEditWigdet)
        self.pythonScriptEditor.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pythonScriptEditor.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.pythonScriptEditor.setAcceptRichText(False)
        self.pythonScriptEditor.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.pythonScriptEditor.setObjectName("pythonScriptEditor")
        self.horizontalLayout_3.addWidget(self.pythonScriptEditor, 0, QtCore.Qt.AlignTop)
        self.execPythonButton = QtWidgets.QPushButton(self.pythonEditWigdet)
        self.execPythonButton.setMinimumSize(QtCore.QSize(75, 50))
        self.execPythonButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.execPythonButton.setObjectName("execPythonButton")
        self.horizontalLayout_3.addWidget(self.execPythonButton)
        self.verticalLayout_5.addWidget(self.pythonEditWigdet)
        self.logsPytoon = QtWidgets.QTextBrowser(self.pythonPage)
        self.logsPytoon.setObjectName("logsPytoon")
        self.verticalLayout_5.addWidget(self.logsPytoon)
        self.clearPythonLogs = QtWidgets.QPushButton(self.pythonPage)
        self.clearPythonLogs.setMinimumSize(QtCore.QSize(0, 30))
        self.clearPythonLogs.setObjectName("clearPythonLogs")
        self.verticalLayout_5.addWidget(self.clearPythonLogs)
        self.pagesWidget.addWidget(self.pythonPage)
        self.downloadFilePage = QtWidgets.QWidget()
        self.downloadFilePage.setObjectName("downloadFilePage")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.downloadFilePage)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.downloadUrl = QtWidgets.QLineEdit(self.downloadFilePage)
        self.downloadUrl.setMinimumSize(QtCore.QSize(0, 30))
        self.downloadUrl.setObjectName("downloadUrl")
        self.verticalLayout_10.addWidget(self.downloadUrl, 0, QtCore.Qt.AlignTop)
        self.downloadButton = QtWidgets.QPushButton(self.downloadFilePage)
        self.downloadButton.setMinimumSize(QtCore.QSize(0, 30))
        self.downloadButton.setObjectName("downloadButton")
        self.verticalLayout_10.addWidget(self.downloadButton, 0, QtCore.Qt.AlignTop)
        self.downloadLogs = QtWidgets.QTextBrowser(self.downloadFilePage)
        self.downloadLogs.setObjectName("downloadLogs")
        self.verticalLayout_10.addWidget(self.downloadLogs)
        self.clearDlLogsButton = QtWidgets.QPushButton(self.downloadFilePage)
        self.clearDlLogsButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clearDlLogsButton.setObjectName("clearDlLogsButton")
        self.verticalLayout_10.addWidget(self.clearDlLogsButton)
        self.pagesWidget.addWidget(self.downloadFilePage)
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.gridLayout = QtWidgets.QGridLayout(self.settingsPage)
        self.gridLayout.setObjectName("gridLayout")
        self.settingsTabWidget = QtWidgets.QTabWidget(self.settingsPage)
        self.settingsTabWidget.setStyleSheet("")
        self.settingsTabWidget.setObjectName("settingsTabWidget")
        self.visualSettingsTab = QtWidgets.QWidget()
        self.visualSettingsTab.setObjectName("visualSettingsTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.visualSettingsTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.chooseAnimationLAbel = QtWidgets.QLabel(self.visualSettingsTab)
        self.chooseAnimationLAbel.setObjectName("chooseAnimationLAbel")
        self.verticalLayout_7.addWidget(self.chooseAnimationLAbel, 0, QtCore.Qt.AlignTop)
        self.chooseAnimationBox = QtWidgets.QComboBox(self.visualSettingsTab)
        self.chooseAnimationBox.setMinimumSize(QtCore.QSize(0, 30))
        self.chooseAnimationBox.setObjectName("chooseAnimationBox")
        self.chooseAnimationBox.addItem("")
        self.chooseAnimationBox.addItem("")
        self.chooseAnimationBox.addItem("")
        self.chooseAnimationBox.addItem("")
        self.chooseAnimationBox.addItem("")
        self.verticalLayout_7.addWidget(self.chooseAnimationBox, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.settingsTabWidget.addTab(self.visualSettingsTab, "")
        self.pusherSettingTab = QtWidgets.QWidget()
        self.pusherSettingTab.setObjectName("pusherSettingTab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pusherSettingTab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pusher_app_id_edit = QtWidgets.QLineEdit(self.pusherSettingTab)
        self.pusher_app_id_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.pusher_app_id_edit.setObjectName("pusher_app_id_edit")
        self.verticalLayout_8.addWidget(self.pusher_app_id_edit)
        self.pusher_key_edit = QtWidgets.QLineEdit(self.pusherSettingTab)
        self.pusher_key_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.pusher_key_edit.setObjectName("pusher_key_edit")
        self.verticalLayout_8.addWidget(self.pusher_key_edit)
        self.pusher_secret_edit = QtWidgets.QLineEdit(self.pusherSettingTab)
        self.pusher_secret_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.pusher_secret_edit.setObjectName("pusher_secret_edit")
        self.verticalLayout_8.addWidget(self.pusher_secret_edit)
        self.pusher_cluster_edit = QtWidgets.QLineEdit(self.pusherSettingTab)
        self.pusher_cluster_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.pusher_cluster_edit.setObjectName("pusher_cluster_edit")
        self.verticalLayout_8.addWidget(self.pusher_cluster_edit)
        self.pushercom_label = QtWidgets.QLabel(self.pusherSettingTab)
        self.pushercom_label.setObjectName("pushercom_label")
        self.verticalLayout_8.addWidget(self.pushercom_label)
        self.settingsTabWidget.addTab(self.pusherSettingTab, "")
        self.imgurSettingsPage = QtWidgets.QWidget()
        self.imgurSettingsPage.setObjectName("imgurSettingsPage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.imgurSettingsPage)
        self.verticalLayout_9.setContentsMargins(-1, 9, 9, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.imgurClientId = QtWidgets.QLineEdit(self.imgurSettingsPage)
        self.imgurClientId.setMinimumSize(QtCore.QSize(0, 30))
        self.imgurClientId.setObjectName("imgurClientId")
        self.verticalLayout_9.addWidget(self.imgurClientId, 0, QtCore.Qt.AlignTop)
        self.imgurLabel = QtWidgets.QLabel(self.imgurSettingsPage)
        self.imgurLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.imgurLabel.setObjectName("imgurLabel")
        self.verticalLayout_9.addWidget(self.imgurLabel, 0, QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.settingsTabWidget.addTab(self.imgurSettingsPage, "")
        self.gridLayout.addWidget(self.settingsTabWidget, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.saveSettingsButton = QtWidgets.QPushButton(self.settingsPage)
        self.saveSettingsButton.setMinimumSize(QtCore.QSize(0, 30))
        self.saveSettingsButton.setObjectName("saveSettingsButton")
        self.gridLayout.addWidget(self.saveSettingsButton, 1, 0, 1, 1)
        self.pagesWidget.addWidget(self.settingsPage)
        self.horizontalLayout.addWidget(self.pagesWidget, 0, QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.leftMenu.setCurrentRow(-1)
        self.pagesWidget.setCurrentIndex(0)
        self.settingsTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "daunRat admin"))
        __sortingEnabled = self.leftMenu.isSortingEnabled()
        self.leftMenu.setSortingEnabled(False)
        item = self.leftMenu.item(0)
        item.setText(_translate("MainWindow", "Menu"))
        item = self.leftMenu.item(1)
        item.setText(_translate("MainWindow", "Devices"))
        item = self.leftMenu.item(2)
        item.setText(_translate("MainWindow", "Screenshot"))
        item = self.leftMenu.item(3)
        item.setText(_translate("MainWindow", "Wallpaper"))
        item = self.leftMenu.item(4)
        item.setText(_translate("MainWindow", "Console"))
        item = self.leftMenu.item(5)
        item.setText(_translate("MainWindow", "Python"))
        item = self.leftMenu.item(6)
        item.setText(_translate("MainWindow", "Download"))
        item = self.leftMenu.item(7)
        item.setText(_translate("MainWindow", "Settings"))
        self.leftMenu.setSortingEnabled(__sortingEnabled)
        self.dLogo.setText(_translate("MainWindow", "D"))
        self.choosePanelLabel.setText(_translate("MainWindow", "Choose panel in left side, scroll menu to see more"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.pingButton.setText(_translate("MainWindow", "Ping"))
        self.reconRefreshButton.setText(_translate("MainWindow", "Reconnect and refresh"))
        self.takeScreenshotButton.setText(_translate("MainWindow", "Take screenshot"))
        self.wallpaperUrlBox.setPlaceholderText(_translate("MainWindow", "Local or web link to wallpaper"))
        self.setWallpaperButton.setText(_translate("MainWindow", "Set wallpaper"))
        self.controlWallpaperEngineLabel.setText(_translate("MainWindow", "Wallpaper Engine control"))
        self.stopWallpaperEngineButton.setText(_translate("MainWindow", "Stop"))
        self.pauseWallpaperEngineButton.setText(_translate("MainWindow", "Pause"))
        self.playWallpaperEngineButton.setText(_translate("MainWindow", "Play"))
        self.muteWallpaperEngineButton.setText(_translate("MainWindow", "Mute"))
        self.unmuteWallpaperEngineButton.setText(_translate("MainWindow", "Unmute"))
        self.wallpaperScreenshotButton.setText(_translate("MainWindow", "Set screenshot as wallpaper"))
        self.daunApWallpaperLabel.setText(_translate("MainWindow", "Use Python Console with daunApi also"))
        self.commandBox.setPlaceholderText(_translate("MainWindow", "Type command here"))
        self.sendCommandButton.setText(_translate("MainWindow", "Send"))
        self.clearConsoleLogs.setText(_translate("MainWindow", "Clear logs"))
        self.pythonScriptEditor.setPlaceholderText(_translate("MainWindow", "os.system(\"systeminfo\")"))
        self.execPythonButton.setText(_translate("MainWindow", "Execute"))
        self.clearPythonLogs.setText(_translate("MainWindow", "Clear logs"))
        self.downloadUrl.setPlaceholderText(_translate("MainWindow", "File url"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.downloadLogs.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.clearDlLogsButton.setText(_translate("MainWindow", "Clear logs"))
        self.chooseAnimationLAbel.setText(_translate("MainWindow", "Choose menu animation"))
        self.chooseAnimationBox.setItemText(0, _translate("MainWindow", "InOutQuart"))
        self.chooseAnimationBox.setItemText(1, _translate("MainWindow", "InOutBack"))
        self.chooseAnimationBox.setItemText(2, _translate("MainWindow", "InOutBounce"))
        self.chooseAnimationBox.setItemText(3, _translate("MainWindow", "OutBack"))
        self.chooseAnimationBox.setItemText(4, _translate("MainWindow", "OutElastic"))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.visualSettingsTab), _translate("MainWindow", "Visual"))
        self.pusher_app_id_edit.setPlaceholderText(_translate("MainWindow", "app_id"))
        self.pusher_key_edit.setPlaceholderText(_translate("MainWindow", "key"))
        self.pusher_secret_edit.setPlaceholderText(_translate("MainWindow", "secret"))
        self.pusher_cluster_edit.setPlaceholderText(_translate("MainWindow", "cluster"))
        self.pushercom_label.setText(_translate("MainWindow", "Create account and application on pusher.com to get this data"))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.pusherSettingTab), _translate("MainWindow", "Pusher"))
        self.imgurClientId.setPlaceholderText(_translate("MainWindow", "client_id"))
        self.imgurLabel.setText(_translate("MainWindow", "Create account on imgur, create app and paste Client ID here"))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.imgurSettingsPage), _translate("MainWindow", "Imgur"))
        self.saveSettingsButton.setText(_translate("MainWindow", "Save settings"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
