import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QVBoxLayout, QPushButton, QDialog)
from PyQt5 import QtCore
from functools import partial
import GameWindow


class ThemeDialog(QDialog):
    def __init__(self):
        super(ThemeDialog, self).__init__()
        self.initUI()

    def initUI(self):
        # self.setFixedSize(800, 700)
        self.label = QLabel("Pick a theme")
        self.btAll = QPushButton(" Mix all Themes ")
        self.btF = QPushButton(" Fruits ")
        self.btM = QPushButton(" Movies ")
        self.btA = QPushButton(" Animals ")

        self.btAll.clicked.connect(partial(self.OpenGameWindow, 'mix'))
        self.btF.clicked.connect(partial(self.OpenGameWindow, 'fruit'))
        self.btM.clicked.connect(partial(self.OpenGameWindow, 'movie'))
        self.btA.clicked.connect(partial(self.OpenGameWindow, 'animal'))

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("QDialog{"
                           "background-color: rgb(59, 161, 218);"
                           "font-size: 60px; font-family: Comic Sans MS;"
                           "}"
                           "QLabel{"
                           "color: white;"
                           "font-size: 62px; font-family: Segoe Print; font-weight:bold;"
                           "}"
                           "QPushButton{"
                           "height: 100px; width: 600px;"
                           "background-color:  rgb(233, 236, 239);"
                           "color: black;"
                           "border-radius: 20px;"
                           "border: 5px solid black;"
                           "font-size: 50px; font-family: Comic Sans MS ; "
                           "}"
                           "QPushButton::hover {"           # [note] No spaces are allowed after the '::'  (orz)
                           "background-color : rgb(255, 183, 3);"
                           "font-size: 55px;"
                           "}")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btAll)
        self.layout.addWidget(self.btF)
        self.layout.addWidget(self.btM)
        self.layout.addWidget(self.btA)
        self.setLayout(self.layout)

    def OpenGameWindow(self, theme):
        self.w = GameWindow.GameWindow(theme)
        self.w.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # know on what OS running and what type of window to open
    dlg = ThemeDialog()
    dlg.show()
    sys.exit(app.exec_())