# Execute this script with the command below to open the GUI
# python run.py

import sys

from PySide2 import QtWidgets
from rodm.ui.run_ui import Main_Dialog
from rodm.ui.splash import Splash_Dialog


def main(args) -> None:
    """
    Main entry point to rodm tool
    Args:
        args: Arguments to pass to QApplication
    """
    if not isinstance(args, list):
        args = list(args)
    app = QtWidgets.QApplication(args)

    ui = Main_Dialog()
    ui.show()

    splash = Splash_Dialog()
    splash.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
