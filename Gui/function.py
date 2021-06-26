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
########################################################################

from PySide6.QtCore import QEasingCurve, QEvent, QPropertyAnimation, Qt, QTimer
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QPushButton, QSizeGrip

TIME_ANIMATION = 500
MAXIMIZED = False
SELECT = """border-left: 13px solid 
    qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.416, y2:0, stop:0.499 #55aaff, stop:0.5 rgba(85, 170, 255, 0));"""


class Function:
    """Trata a estilização da interface"""

    # Recebe o objeto pai
    def __init__(self, parent: object):
        self._parent = parent

    def setDevelopVersion(self, develop: str, version: str):
        """Define texto nas label de desenvolvedor e versão."""

        self._parent.labelDevelop.setText(develop)
        self._parent.labelVersion.setText(version)

    def setAppName(self, name: str):
        self._parent.labelAppName.setText(name)

    def setPosition(self, event):
        """Recebe a posição do mouse. Usado para complemetar
        a função que movimenta a janela"""

        self._parent.dragPos = event.globalPos()

    def setGrip(self):
        """Define os Grip para redimensionamento da janela"""

        self._parent.sizegrip = QSizeGrip(self._parent.frGrip)
        self._parent.sizegrip.setStyleSheet("width: 23px; height: 20px; margin 0px; padding: 0px;")

    # Remove bordas e background do objeto
    def removeCentralWidget(self):
        self._parent.setWindowFlags(Qt.FramelessWindowHint)
        self._parent.setAttribute(Qt.WA_TranslucentBackground)

    # Define uma sombra ao widget
    def setDropShadow(self, widget: object):
        self._parent.shadow = QGraphicsDropShadowEffect(self._parent)
        self._parent.shadow.setBlurRadius(17)
        self._parent.shadow.setXOffset(0)
        self._parent.shadow.setYOffset(0)
        self._parent.shadow.setColor(QColor(0, 0, 0, 150))
        widget.setGraphicsEffect(self._parent.shadow)

    # Maximiza e Restaura a janela
    def maximizeRestore(self):

        global MAXIMIZED

        if MAXIMIZED == False:
            self._parent.showMaximized()
            MAXIMIZED = True
            self._parent.gridLayout.setContentsMargins(0, 0, 0, 0)
            self._parent.btMax.setToolTip("Restaurar")
            self._parent.btMax.setIcon(QIcon(":/16x16/16x16/cil-restore.png"))
            self._parent.frGrip.hide()

        else:
            MAXIMIZED = False
            self._parent.showNormal()
            self._parent.resize(self._parent.width() + 1, self._parent.height() + 1)
            self._parent.gridLayout.setContentsMargins(10, 10, 10, 10)
            self._parent.btMax.setToolTip("Maximizar")
            self._parent.btMax.setIcon(QIcon(":/16x16/16x16/cil-media-stop.png"))
            self._parent.frGrip.show()

    # Maximiza a janela
    def dobleClickMaximizeRestore(self, event):
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, lambda: self.maximizeRestore())

    # Move a janela
    def moveWindow(self, event):

        # Restaura o tamanho da janela quando maximizada
        if MAXIMIZED:
            self.maximizeRestore()

        if event.buttons() == Qt.LeftButton:
            self._parent.move(self._parent.pos() + event.globalPos() - self._parent.dragPos)
            self._parent.dragPos = event.globalPos()
            event.accept()

    # Alterna a largura do frame
    def extendFrame(self, maxWidth: int, frame: object):

        # obtem a largura
        width = frame.width()
        width_standard = 50

        # Define a maxima largura
        if width == width_standard:
            widthExtended = maxWidth

        else:
            widthExtended = width_standard

        # Animação
        self._parent.animation = QPropertyAnimation(frame, b"minimumWidth")
        self._parent.animation.setDuration(TIME_ANIMATION)
        self._parent.animation.setStartValue(width)
        self._parent.animation.setEndValue(widthExtended)
        self._parent.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self._parent.animation.start()

    # Define folhas de estilos para a aplicação
    def setStyleTheme(self, theme_file: str):
        theme = open(theme_file, "r").read()
        self._parent.setStyleSheet(theme)

    # Destaca o botão que foi selecionado
    def setButtomSelect(self, buttom: QPushButton):
        for widget in self._parent.frMenuLateral.findChildren(QPushButton):
            if widget.objectName() == buttom.objectName():
                widget.setStyleSheet(SELECT)
            else:
                widget.setStyleSheet("")
