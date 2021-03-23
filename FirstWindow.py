from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QGroupBox, QVBoxLayout, QGridLayout, QWidget, QPushButton, QDesktopWidget, QApplication,
                             QLabel)
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QFont
import Theme
import sys


class FirstWindow(QWidget):
    # First window the user opens
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000, 600)
        self.center()
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.setWindowTitle("The Hangman")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./image/background.png")))
        self.setPalette(palette)

        # Label of welcome text
        self.textin = QLabel(self)
        self.textin.setText("\nWelcome to Hangman!")
        self.textin.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("QLabel{"
                           # "color:rgb(0, 0, 0, 180);"
                           # "background-color: rgb(0, 0, 0, 20);"
                           "color: rgb(59, 161, 218);" 
                           "font-family:Kristen ITC; font-size:100px"
                           "}"
                           "QPushButton{"
                           "color: rgb(0, 0, 0, 200);"
                           "background-color:rgb(255, 255, 255, 0);"
                           "border:none;"
                           "font-family:Kristen ITC; font-size:40px;"
                           "}"
                           "QPushButton::hover{"
                           "color: rgb(59, 161, 218);"
                           "font-size:45px;"
                           "}")

        # PlaceHolder for Hangman
        self.img = QPixmap("./image/0.png")
        self.labelImg = QLabel()
        self.labelImg.setPixmap(self.img)
        self.labelImg.setAlignment(QtCore.Qt.AlignCenter)
        # self.labelImg.setScaledContents(True)

        # Button to start the game
        self.bt1 = QPushButton(self)
        self.bt1.setText("[Start]")
        self.bt1.clicked.connect(self.OpenThemeDialog)

        # Button to quit the game
        self.bt2 = QPushButton(self)
        self.bt2.setText("[Quit]")
        self.bt2.clicked.connect(self.GameQuit)

        # Grid
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.addWidget(self.textin, 0, 0, 1, 0)
        layout.addWidget(self.labelImg, 1, 0, 1, 0)
        layout.addWidget(self.bt1, 2, 0)
        layout.addWidget(self.bt2, 2, 1)

        self.horizontalGroupBox.setLayout(layout)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.showMaximized()

    def center(self):
        # Function to center window
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def OpenThemeDialog(self):
        # Function Opening "Pick Theme Dialog"
        # self.w = GameWindow.GameWindow('fruit')
        # self.w.show()
        self.d = Theme.ThemeDialog()
        self.d.show()
        # self.close()

    def GameQuit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FirstWindow()
    win.show()
    sys.exit(app.exec_())
