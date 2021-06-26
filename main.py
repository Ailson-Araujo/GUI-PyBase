########################################################################
## Copyright © 2021, Ailson Araujo
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
## Versão: 1.0
##
## Projeto feito com Qt Designer, PySide6.
## Baseado no projeto de WANDERSON M.PIMENTA
########################################################################

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
        function.setAppName("Sua Aplicação")
        function.setStyleTheme("stylesheet/base_dark.qss")

        self.stackedWidget.setCurrentIndex(0)

        self.frTitleBar.mouseDoubleClickEvent = function.dobleClickMaximizeRestore
        self.frTitleBar.mouseMoveEvent = function.moveWindow
        self.setDesignerSelectedButton(function)

        self.btMin.clicked.connect(lambda: self.showMinimized())
        self.btMax.clicked.connect(lambda: function.maximizeRestore())
        self.btClose.clicked.connect(lambda: self.close())

        self.btHide.clicked.connect(lambda: function.extendFrame(190, self.frMenuLateral))
        self.bt.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.bt2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    def setDesignerSelectedButton(self, function: object):
        self.bt.clicked.connect(lambda: function.setButtonSelected(self.bt))
        self.bt2.clicked.connect(lambda: function.setButtonSelected(self.bt2))
        self.bt3.clicked.connect(lambda: function.setButtonSelected(self.bt3))
        self.btSettings.clicked.connect(lambda: function.setButtonSelected(self.btSettings))

    def mousePressEvent(self, event):
        function = Function(self)
        function.setPosition(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinPyBase()
    win.show()
    sys.exit(app.exec())
