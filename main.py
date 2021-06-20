import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

import Gui.guiFunction as function
import Gui.resource_rc
from Gui.pyBase import Ui_PyBase


class WinPyBase(QMainWindow, Ui_PyBase):
    def __init__(self, *args, obj=None, **kargs):
        super(WinPyBase, self).__init__(*args, **kargs)
        self.setupUi(self)

        function.setObject(self)
        function.setGrip(self)
        function.setDropShadow(self, self.frBase)
        function.removeCentralWidget(self)

        self.frTitleBar.mouseDoubleClickEvent = function.dobleClickMaximizeRestore
        self.frTitleBar.mouseMoveEvent = function.moveWindow

        self.btMin.clicked.connect(lambda: self.showMinimized())
        self.btMax.clicked.connect(lambda: function.maximizeRestore(self))
        self.btClose.clicked.connect(lambda: self.close())

        self.bt.clicked.connect(lambda: function.extendMenu(self, 190, self.frMenuLateral))

    def mousePressEvent(self, event):
        function.setPosition(self, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinPyBase()
    win.show()
    sys.exit(app.exec())
