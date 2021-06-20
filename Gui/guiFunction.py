from PySide6.QtCore import QEasingCurve, QEvent, QPropertyAnimation, Qt, QTimer
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip

TIME_ANIMATION = 500
MAXIMIZED = False
SELF = None


def setObject(self):
    """Define um Objeto global para eventos onde não se
    pode passar o objeto como parâmetro"""

    global SELF
    SELF = self


def setPosition(self, event):
    """Recebe a posição do mouse usado para complemetar
    a função que movimenta a janela"""

    SELF.dragPos = event.globalPos()


def setGrip(self):
    """Define os Grip para redimensionamento da janela"""

    self.sizegrip = QSizeGrip(self.frGrip)


# Remove moldura e background do objeto
def removeCentralWidget(self):
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setAttribute(Qt.WA_TranslucentBackground)


# Define uma sombra ao widget
def setDropShadow(self, widget):
    self.shadow = QGraphicsDropShadowEffect(self)
    self.shadow.setBlurRadius(17)
    self.shadow.setXOffset(0)
    self.shadow.setYOffset(0)
    self.shadow.setColor(QColor(0, 0, 0, 150))
    widget.setGraphicsEffect(self.shadow)


# Construção
def maximizeRestore(self):

    global MAXIMIZED

    if MAXIMIZED == False:
        self.showMaximized()
        MAXIMIZED = True
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btMax.setToolTip("Restaurar")
        self.btMax.setIcon(QIcon(u":/16x16/16x16/cil-restore.png"))
        self.frGrip.hide()

    else:
        MAXIMIZED = False
        self.showNormal()
        self.resize(self.width() + 1, self.height() + 1)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.btMax.setToolTip("Maximizar")
        self.btMax.setIcon(QIcon(u":/16x16/16x16/cil-media-stop.png"))
        self.frGrip.show()


# Maximiza a janela
def dobleClickMaximizeRestore(event):
    if event.type() == QEvent.MouseButtonDblClick:
        QTimer.singleShot(250, lambda: maximizeRestore(SELF))


# Move a janela
def moveWindow(event):

    # Restaura o tamanho da janela quando
    # quando maximizada
    if MAXIMIZED:
        maximizeRestore(SELF)

    if event.buttons() == Qt.LeftButton:
        SELF.move(SELF.pos() + event.globalPos() - SELF.dragPos)
        SELF.dragPos = event.globalPos()
        event.accept()


# Alterna a largura do menu
def extendMenu(self, maxWidth, frame):

    # obtem a largura
    width = frame.width()
    width_standard = 50

    # Define a maxima largura
    if width == width_standard:
        widthExtended = maxWidth

    else:
        widthExtended = width_standard

    # Animação
    self.animation = QPropertyAnimation(frame, b"minimumWidth")
    self.animation.setDuration(TIME_ANIMATION)
    self.animation.setStartValue(width)
    self.animation.setEndValue(widthExtended)
    self.animation.setEasingCurve(QEasingCurve.InOutQuart)
    self.animation.start()
