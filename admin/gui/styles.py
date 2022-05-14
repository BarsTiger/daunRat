centralwidget = """
QWidget {
    background-color: rgb(30, 30, 30);
    color: rgb(255, 255, 255);
    font: 10pt "Segoe UI";
}


QScrollBar:vertical,
QScrollBar:horizontal {
    border: none;
    background: rgb(30, 30, 30);
    width: 10px;
    margin: 15px 0 15px 0;
    border-radius: 0px;
}

QScrollBar::handle:vertical,
QScrollBar::handle:horizontal {	
    background-color: rgb(139, 139, 139);
    min-height: 30px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover,
QScrollBar::handle:vertical:pressed,
QScrollBar::handle:horizontal:hover,
QScrollBar::handle:horizontal:pressed {	
    background-color: rgb(149, 149, 149);
}

QScrollBar::sub-line:vertical,
QScrollBar::add-line:vertical,
QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical {
    height: 0px;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical, 
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}


QPushButton {
    color: white;
    border-width: 1px;
    border-radius:6px;
    border-style: solid;
    border-color: #303030;
    background-color: #2c2d2e;
}
QPushButton:hover {
    border-width: 2px;
    background-color: #323232;
}
QPushButton:pressed {
    background-color: #262728;
}
QPushButton:disabled {
    background-color: #434343;
    border-color: #0000;
}


QLineEdit, QTextBrowser, QPlainTextEdit, QTextEdit {
    border-width: 1px;
    border-radius: 5px;
    border-style: solid;
    border-color: #303030;
    background-color: #242424;
    font: 10pt "Segoe UI";
}


QListWidget {
    border-width: 1px;
    border-radius: 15px;
    border-style: solid;
    border-color: #303030;
    padding: 10px;
    background-color: #242424;
    font: 10pt "Segoe UI";
}
QListWidget:item {
    background-color: #242424;
    selection-color: white;
}
QListWidget:item:hover {
    background-color: #323232;
}
QListWidget:item:selected {
    background-color: #777777;
}
"""

menupage = """
QListWidget {
    border-width: 0px;
    border-radius: 0px;
    border: none;
    padding: 0px;
    background-color: #242424;
    font: 10pt "Segoe UI";
}
QListWidget:item {
    padding-left: 10px;
    height: 60px;
    background-color: #191919;
    selection-color: rgba(255, 255, 255);
}
QListWidget:item:hover {
    background-color: #323232;
}
QListWidget:item:selected {
    background-color: #262728;
}
"""
