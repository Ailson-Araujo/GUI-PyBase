from PySide6.QtCore import QEasingCurve, QEvent, QPropertyAnimation, Qt, QTimer
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip

TIME_ANIMATION = 500
MAXIMIZED = False


class Function:
    """Trata a estilização da interface"""

    # Recebe o objeto pai
    def __init__(self, parent: object):
        self._parent = parent

    def setDevelopVersion(self, develop: str, version: str):
        """Define texto nas label de desenvolvedor e versão."""

        self._parent.labelDevelop.setText(develop)
        self._parent.labelVersion.setText(version)

    def setPosition(self, event):
        """Recebe a posição do mouse. Usado para complemetar
        a função que movimenta a janela"""

        self._parent.dragPos = event.globalPos()

    def setGrip(self):
        """Define os Grip para redimensionamento da janela"""

        self._parent.sizegrip = QSizeGrip(self._parent.frGrip)

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
            self._parent.btMax.setIcon(QIcon(u":/16x16/16x16/cil-restore.png"))
            self._parent.frGrip.hide()

        else:
            MAXIMIZED = False
            self._parent.showNormal()
            self._parent.resize(self._parent.width() + 1, self._parent.height() + 1)
            self._parent.gridLayout.setContentsMargins(10, 10, 10, 10)
            self._parent.btMax.setToolTip("Maximizar")
            self._parent.btMax.setIcon(QIcon(u":/16x16/16x16/cil-media-stop.png"))
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
