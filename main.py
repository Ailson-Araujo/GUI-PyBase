import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

import Gui.resource_rc
from Gui.function import Function
from Gui.pyBase import Ui_PyBase

__version__ = "1.0"
__develop__ = "Ailson Araujo"

# Para problema de alto DPI e escala acima de 100%
os.environ["QT_FONT_DPI"] = "96"


class WinPyBase(QMainWindow, Ui_PyBase):
    def __init__(self, *args, obj=None, **kargs):
        super(WinPyBase, self).__init__(*args, **kargs)
        self.setupUi(self)

        function = Function(self)
        function.setGrip()
        function.setDropShadow(self.frBase)
        function.removeCentralWidget()
        function.setDevelopVersion(__develop__, __version__)

        self.frTitleBar.mouseDoubleClickEvent = function.dobleClickMaximizeRestore
        self.frTitleBar.mouseMoveEvent = function.moveWindow

        self.btMin.clicked.connect(lambda: self.showMinimized())
        self.btMax.clicked.connect(lambda: function.maximizeRestore())
        self.btClose.clicked.connect(lambda: self.close())

        self.btHide.clicked.connect(lambda: function.extendFrame(190, self.frMenuLateral))

    def mousePressEvent(self, event):
        function = Function(self)
        function.setPosition(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinPyBase()
    win.show()
    sys.exit(app.exec())
