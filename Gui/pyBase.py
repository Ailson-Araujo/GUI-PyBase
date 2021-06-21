# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyBase.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import Gui.resource_rc


class Ui_PyBase(object):
    def setupUi(self, PyBase):
        if not PyBase.objectName():
            PyBase.setObjectName(u"PyBase")
        PyBase.resize(805, 540)
        self.centralwidget = QWidget(PyBase)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.frBase = QFrame(self.centralwidget)
        self.frBase.setObjectName(u"frBase")
        self.frBase.setFrameShape(QFrame.StyledPanel)
        self.frBase.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frBase)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frMenuLateral = QFrame(self.frBase)
        self.frMenuLateral.setObjectName(u"frMenuLateral")
        self.frMenuLateral.setMinimumSize(QSize(50, 0))
        self.frMenuLateral.setMaximumSize(QSize(50, 16777215))
        self.frMenuLateral.setStyleSheet(u"")
        self.frMenuLateral.setFrameShape(QFrame.StyledPanel)
        self.frMenuLateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frMenuLateral)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btHide = QPushButton(self.frMenuLateral)
        self.btHide.setObjectName(u"btHide")
        self.btHide.setMinimumSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btHide)

        self.bt = QPushButton(self.frMenuLateral)
        self.bt.setObjectName(u"bt")
        self.bt.setMinimumSize(QSize(50, 50))
        self.bt.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.bt)

        self.bt2 = QPushButton(self.frMenuLateral)
        self.bt2.setObjectName(u"bt2")
        self.bt2.setMinimumSize(QSize(50, 50))
        self.bt2.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.bt2)

        self.bt3 = QPushButton(self.frMenuLateral)
        self.bt3.setObjectName(u"bt3")
        self.bt3.setMinimumSize(QSize(50, 50))
        self.bt3.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.bt3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btSettings = QPushButton(self.frMenuLateral)
        self.btSettings.setObjectName(u"btSettings")
        self.btSettings.setMinimumSize(QSize(50, 50))
        self.btSettings.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.btSettings)

        self.gridLayout_2.addWidget(self.frMenuLateral, 2, 0, 2, 1)

        self.frContent = QFrame(self.frBase)
        self.frContent.setObjectName(u"frContent")
        self.frContent.setStyleSheet(u"")
        self.frContent.setFrameShape(QFrame.StyledPanel)
        self.frContent.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frContent)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.frContent)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.frContent, 2, 1, 1, 3)

        self.frTitleBar = QFrame(self.frBase)
        self.frTitleBar.setObjectName(u"frTitleBar")
        self.frTitleBar.setMinimumSize(QSize(0, 40))
        self.frTitleBar.setMaximumSize(QSize(16777215, 40))
        self.frTitleBar.setStyleSheet(u"")
        self.frTitleBar.setFrameShape(QFrame.StyledPanel)
        self.frTitleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frTitleBar)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 5, 0)
        self.frIcon = QFrame(self.frTitleBar)
        self.frIcon.setObjectName(u"frIcon")
        self.frIcon.setMinimumSize(QSize(50, 40))
        self.frIcon.setMaximumSize(QSize(50, 50))
        self.frIcon.setFrameShape(QFrame.StyledPanel)
        self.frIcon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frIcon)

        self.labelAppName = QLabel(self.frTitleBar)
        self.labelAppName.setObjectName(u"labelAppName")

        self.horizontalLayout.addWidget(self.labelAppName)

        self.horizontalSpacer = QSpacerItem(371, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btMin = QPushButton(self.frTitleBar)
        self.btMin.setObjectName(u"btMin")
        self.btMin.setMinimumSize(QSize(30, 30))
        self.btMin.setMaximumSize(QSize(30, 30))
        self.btMin.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/16x16/16x16/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btMin.setIcon(icon)

        self.horizontalLayout.addWidget(self.btMin)

        self.btMax = QPushButton(self.frTitleBar)
        self.btMax.setObjectName(u"btMax")
        self.btMax.setMinimumSize(QSize(30, 30))
        self.btMax.setMaximumSize(QSize(30, 30))
        self.btMax.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/16x16/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btMax.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btMax)

        self.btClose = QPushButton(self.frTitleBar)
        self.btClose.setObjectName(u"btClose")
        self.btClose.setMinimumSize(QSize(30, 30))
        self.btClose.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.btClose.setFont(font)
        self.btClose.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btClose.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btClose)

        self.gridLayout_2.addWidget(self.frTitleBar, 1, 0, 1, 4)

        self.frStatusBar = QFrame(self.frBase)
        self.frStatusBar.setObjectName(u"frStatusBar")
        self.frStatusBar.setMaximumSize(QSize(16777215, 22))
        self.frStatusBar.setStyleSheet(u"")
        self.frStatusBar.setFrameShape(QFrame.StyledPanel)
        self.frStatusBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frStatusBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelDevelop = QLabel(self.frStatusBar)
        self.labelDevelop.setObjectName(u"labelDevelop")

        self.horizontalLayout_2.addWidget(self.labelDevelop)

        self.horizontalSpacer_2 = QSpacerItem(487, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.labelVersion = QLabel(self.frStatusBar)
        self.labelVersion.setObjectName(u"labelVersion")

        self.horizontalLayout_2.addWidget(self.labelVersion)

        self.frGrip = QFrame(self.frStatusBar)
        self.frGrip.setObjectName(u"frGrip")
        self.frGrip.setMinimumSize(QSize(22, 22))
        self.frGrip.setMaximumSize(QSize(22, 22))
        self.frGrip.setStyleSheet(
            u"/*QFrame{\n"
            "	background-image: url(:/16x16/16x16/cil-size-grip.png);\n"
            "    background-repeat: no-repeat;\n"
            "	background-color: transparent;\n"
            "    background-position: right bottom;\n"
            "    margin: 3px 1px;\n"
            "}*/"
        )
        self.frGrip.setFrameShape(QFrame.StyledPanel)
        self.frGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frGrip)

        self.gridLayout_2.addWidget(self.frStatusBar, 3, 1, 1, 3)

        self.gridLayout.addWidget(self.frBase, 1, 0, 1, 1)

        PyBase.setCentralWidget(self.centralwidget)

        self.retranslateUi(PyBase)

        QMetaObject.connectSlotsByName(PyBase)

    # setupUi

    def retranslateUi(self, PyBase):
        PyBase.setWindowTitle(QCoreApplication.translate("PyBase", u"MainWindow", None))
        self.btHide.setText(QCoreApplication.translate("PyBase", u"Menu", None))
        self.bt.setText(QCoreApplication.translate("PyBase", u"PushButton", None))
        self.bt2.setText(QCoreApplication.translate("PyBase", u"PushButton", None))
        self.bt3.setText(QCoreApplication.translate("PyBase", u"PushButton", None))
        self.btSettings.setText(QCoreApplication.translate("PyBase", u"PushButton", None))
        self.labelAppName.setText(QCoreApplication.translate("PyBase", u"App", None))
        # if QT_CONFIG(tooltip)
        self.btMin.setToolTip(QCoreApplication.translate("PyBase", u"Minimizar", None))
        # endif // QT_CONFIG(tooltip)
        self.btMin.setText("")
        # if QT_CONFIG(tooltip)
        self.btMax.setToolTip(QCoreApplication.translate("PyBase", u"Maximizar", None))
        # endif // QT_CONFIG(tooltip)
        self.btMax.setText("")
        # if QT_CONFIG(tooltip)
        self.btClose.setToolTip(QCoreApplication.translate("PyBase", u"Fechar", None))
        # endif // QT_CONFIG(tooltip)
        self.btClose.setText("")
        self.labelDevelop.setText(QCoreApplication.translate("PyBase", u"develop", None))
        self.labelVersion.setText(QCoreApplication.translate("PyBase", u"version", None))

    # retranslateUi
