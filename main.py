from PyQt5.QtWidgets import QApplication
import sys
import FirstWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FirstWindow.FirstWindow()
    win.show()
    sys.exit(app.exec_())
