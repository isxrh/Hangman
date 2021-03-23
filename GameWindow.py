import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QGroupBox, QVBoxLayout, QMessageBox,
                             QGridLayout, QWidget, QPushButton, QDesktopWidget)
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
from functools import partial
import Player
import Solution
import Theme


class GameWindow(QWidget):
    def __init__(self, theme):
        super(GameWindow, self).__init__()
        global User
        User = Player.Player()
        global SolutionMain
        SolutionMain = Solution.Solution(theme)
        self.initUI()
        self.resetVariables()

    def initUI(self):
        # set window style
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.setWindowTitle("The Hangman")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./image/background.png")))
        self.setPalette(palette)

        # Button style:
        self.setStyleSheet("QPushButton{"
                           "height: 60px;"
                           "background-color : rgb(59, 161, 218);"
                           "color: white;"
                           "border-style: solid; border-radius: 30px;"
                           "font-size: 40px;"
                           "font-family: HGYT2_CNKI, HGYT1_CNKI ; "
                           "}"
                           "QPushButton::hover {"
                           "background-color: rgb(34, 128, 191);"
                           "font-size: 45px;"
                           "}"
                           "QPushButton::disabled"
                           "{"
                           "background-color : white;"
                           "color: rgb(165, 165, 165);"
                           "border: 3px solid rgb(165, 165, 165);"
                           "}"
                           )

        # Button to exit game
        self.exitBt = QPushButton(" Exit ")
        self.exitBt.clicked.connect(self.close)
        self.exitBt.setStyleSheet("QPushButton{"
                                  # "background-color : rgb(246, 170, 28);"
                                  # "background-color : rgb(255,255,255);"
                                  "background-color : rgb(246, 170, 28);"
                                  "height: 40px;"
                                  "line-height: 40px;"
                                  "font-size: 30px;"
                                  "border-style: solid; border-radius: 18px;"
                                  "}"
                                  "QPushButton::hover {"
                                  "background-color: rgb(255, 145, 0);"
                                  "font-size: 32px;"
                                  "}")

        # Button to change theme
        self.changeBt = QPushButton("  Change theme  ")
        self.changeBt.clicked.connect(self.changeTheme)
        self.changeBt.setStyleSheet("QPushButton{"
                                  # "background-color : rgb(246, 170, 28);"
                                  # "background-color : rgb(255,255,255);"
                                  "background-color : rgb(246, 170, 28);"
                                  "height: 40px;"
                                  "line-height: 40px;"
                                  "font-size: 30px;"
                                  "border-style: solid; border-radius: 18px;"
                                  "}"
                                  "QPushButton::hover {"
                                  "background-color: rgb(255, 145, 0);"
                                  "font-size: 32px;"
                                  "}")

        # Button to check the Solution
        self.solutionBt = QPushButton(self)
        self.solutionBt.setText(" Answer ")
        self.solutionBt.clicked.connect(self.clickedSolution)
        self.solutionBt.setStyleSheet("QPushButton{"
                                      "background-color : rgb(246, 170, 28);"
                                      "height: 40px;"
                                      "font-size: 30px;"
                                      "border-style: solid; border-radius: 18px;"
                                      # "line-height: 200%;"
                                      # "line-height: 40px;"
                                      "}"
                                      "QPushButton::hover {"
                                      "background-color: rgb(255, 145, 0);"
                                      "font-size: 32px;"
                                      "}")

        # PlaceHolder for the word
        self.solution = QLabel(self)
        self.solution.setText(SolutionMain.hiddenSolution)
        self.solution.setAlignment(QtCore.Qt.AlignCenter)  # 居中
        self.solution.setStyleSheet("QLabel{"
                                    "font-size: 80px;"
                                    # "letter-spacing: 20pt;"
                                    "font-family: HGYT2_CNKI, HGYT1_CNKI ;"
                                    "color: rgb(0, 0, 0, 200)"
                                    "}")

        # PlaceHolder for Hangman
        self.img = QPixmap("./image/0.png")
        self.labelImg = QLabel()
        self.labelImg.setPixmap(self.img)

        # PlaceHolder for letter button
        self.letters = []
        for i in range(26):
            self.letters.append(QPushButton(chr(ord('A') + i)))
            # self.letters[i].clicked.connect(lambda: self.clickedLetter(k))
            self.letters[i].clicked.connect(partial(self.clickedCheck, chr(ord('A') + i)))
        self.letterGoupBox = QGroupBox("")
        letterLayout = QGridLayout()
        for i in range(3):
            if i == 2:
                for k in range(8):
                    letterLayout.addWidget(self.letters[i * 9 + k], i, k)
            else:
                for j in range(9):
                    letterLayout.addWidget(self.letters[i * 9 + j], i, j)
        self.letterGoupBox.setLayout(letterLayout)

        # Grid line
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        layout.addWidget(self.exitBt, 0, 1)
        layout.addWidget(self.changeBt, 1, 1)
        layout.addWidget(self.solutionBt, 2, 1)
        layout.addWidget(self.solution, 2, 3, 2, 8)
        layout.addWidget(self.labelImg, 4, 0, 1, 3)
        layout.addWidget(self.letterGoupBox, 4, 3, 1, 8)
        self.horizontalGroupBox.setLayout(layout)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.showMaximized()

    def resetVariables(self):
        self.UserInput = ""
        User.resetPlayer()
        SolutionMain.resetSolution()
        self.solution.setText(SolutionMain.hiddenSolution)
        self.labelImg.setPixmap(QPixmap("./image/0.png"))
        for i in range(26):
            self.letters[i].setEnabled(True)

    def center(self):
        # Function to center window
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clickedSolution(self):
        # Function to show the right Solution
        self.solution.setText(SolutionMain.Solution)
        User.lostGame = True
        User.currentLife = 0
        self.Hangman()
        for i in range(26):
            self.letters[i].setDisabled(True)
        self.errorMessage("ANSWER: " + SolutionMain.Solution)

    def changeTheme(self):
        self.close()
        self.t = Theme.ThemeDialog()
        self.t.show()

    def clickedCheck(self, letterClicked):
        print(letterClicked)
        self.letters[ord(letterClicked) - ord('A')].setDisabled(True)
        User.userInput.append(letterClicked)
        # Replace the label of Player Input
        # self.label.setText(' '.join(str(i) for i in User.userInput))
        # Raplace the solution
        SolutionMain.CheckIfInWord(letterClicked)  # len will be 0 if the solution is not inside
        # Checking if the solution is inside!
        if len(SolutionMain.LettersIn) == 0:
            User.loosingLife()
            self.Hangman()
            self.LostTheGame()
        else:
            self.solution.setText(SolutionMain.hiddenSolution)
            # self.update()
            if SolutionMain.hiddenSolution == SolutionMain.Solution:
                self.errorMessage("CONGRATULATIONS!")
                # self.b1.setText("Close to quit the game")

    def errorMessage(self, errormsg):
        # Manage the structure of the error message
        msgbox = QMessageBox()
        msgbox.setText(errormsg)
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgbox.button(QMessageBox.Yes).setText(' Quit Game ')
        msgbox.button(QMessageBox.No).setText(' New Game ')
        msgbox.button(QMessageBox.Yes).clicked.connect(self.GameQuit)
        msgbox.button(QMessageBox.No).clicked.connect(self.NewGame)
        msgbox.setWindowFlag(Qt.FramelessWindowHint)

        # style
        msgbox.setStyleSheet("QMessageBox {"
                             # "background-color: rgb(206, 211, 220);"
                             # "background-color: rgb(203, 229, 246);"
                             "background-color: rgb(238, 246, 252);"
                             "color: white;"
                             "font-size: 60px; font-family:Kristen ITC; "
                             # "height: 80px;"
                             "border-style: solid; border-radius: 25px; "
                             "box-shadow: 2px 2px 2px 1px rgb(0, 0, 0, 100);"
                             "}"
                             "QPushButton {"
                             # "background-color : rgb(203, 229, 246);"
                             "background-color : rgb(151, 202, 237);"
                             "height: 40px;"
                             "font-size: 25px; font-family: HGYT2_CNKI;"
                             "border-style: solid; border-radius: 14px;"
                             "color: rgb(0, 0, 0, 200)"
                             "}"
                             "QPushButton::hover {"
                             "background-color: rgb(99, 176, 227);"
                             "font-size: 26px;"
                             "}")
        msgbox.exec_()

    def GameQuit(self):
        self.close()

    def NewGame(self):
        self.resetVariables()
        # self.initUI()

    def LostTheGame(self):
        if User.lostGame == True:
            for i in range(26):
                self.letters[i].setDisabled(True)
            self.solution.setText(SolutionMain.Solution)
            self.errorMessage("GAME OVER!")
        else:
            pass
            # self.errormessage("The letter wasn't in the word!")

    def Hangman(self):
        self.img = QPixmap("./image/" + str(7 - User.currentLife) + ".png")
        self.labelImg.setPixmap(self.img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GameWindow('fruit')
    win.show()
    sys.exit(app.exec_())
