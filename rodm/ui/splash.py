from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QMainWindow
from rodm.ui.splash_ui import Ui_Dialog as Splash_UI


class Splash_Dialog(QMainWindow, Splash_UI):
    def __init__(self):
        QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.center_screen()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def center_screen(self):
        size = self.size()
        desktopSize = QtWidgets.QDesktopWidget().screenGeometry()
        top = (desktopSize.height() / 2) - (size.height() / 2)
        left = (desktopSize.width() / 2) - (size.width() / 2)
        self.move(left, top)

    def btn_close_clicked(self):
        self.close()
