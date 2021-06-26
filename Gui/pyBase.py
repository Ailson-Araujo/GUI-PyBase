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
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 25))

        self.gridLayout_5.addWidget(self.spinBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 18))

        self.gridLayout_5.addWidget(self.radioButton, 0, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(0, 25))

        self.gridLayout_5.addWidget(self.doubleSpinBox, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 18))

        self.gridLayout_5.addWidget(self.checkBox, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 3, 1)

        self.horizontalScrollBar = QScrollBar(self.page_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalScrollBar, 0, 1, 1, 3)

        self.horizontalSlider = QSlider(self.page_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider, 1, 1, 1, 3)

        self.verticalScrollBar = QScrollBar(self.page_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalScrollBar, 2, 1, 4, 1)

        self.verticalSlider = QSlider(self.page_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider, 2, 2, 4, 1)

        self.tableWidget = QTableWidget(self.page_2)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 21):
            self.tableWidget.setRowCount(21)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.tableWidget, 2, 3, 4, 1)

        self.comboBox = QComboBox(self.page_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.comboBox, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 22))
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit, 4, 0, 1, 1)

        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_4.addWidget(self.textEdit, 5, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)


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
        self.frGrip.setStyleSheet(u"/*QFrame{\n"
"	background-image: url(:/16x16/16x16/cil-size-grip.png);\n"
"    background-repeat: no-repeat;\n"
"	background-color: transparent;\n"
"    background-position: right bottom;\n"
"    margin: 3px 1px;\n"
"}*/")
        self.frGrip.setFrameShape(QFrame.StyledPanel)
        self.frGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frGrip)


        self.gridLayout_2.addWidget(self.frStatusBar, 3, 1, 1, 3)


        self.gridLayout.addWidget(self.frBase, 1, 0, 1, 1)

        PyBase.setCentralWidget(self.centralwidget)

        self.retranslateUi(PyBase)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(PyBase)
    # setupUi

    def retranslateUi(self, PyBase):
        PyBase.setWindowTitle(QCoreApplication.translate("PyBase", u"MainWindow", None))
        self.btHide.setText(QCoreApplication.translate("PyBase", u"Menu", None))
        self.bt.setText(QCoreApplication.translate("PyBase", u"PushButton", None))
        self.bt2.setText(QCoreApplication.translate("PyBase", u"PushButton", None))
        self.bt3.setText(QCoreApplication.translate("PyBase", u"PushButton", None))
        self.btSettings.setText(QCoreApplication.translate("PyBase", u"PushButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("PyBase", u"GroupBox", None))
        self.radioButton.setText(QCoreApplication.translate("PyBase", u"RadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("PyBase", u"CheckBox", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PyBase", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PyBase", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PyBase", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(20)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("PyBase", u"New Row", None));
        self.comboBox.setItemText(0, QCoreApplication.translate("PyBase", u"New Item", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("PyBase", u"New Item", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("PyBase", u"New Item", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("PyBase", u"New Item", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("PyBase", u"New Item", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("PyBase", u"New Item", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("PyBase", u"New Item", None))

        self.labelAppName.setText(QCoreApplication.translate("PyBase", u"App", None))
#if QT_CONFIG(tooltip)
        self.btMin.setToolTip(QCoreApplication.translate("PyBase", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.btMin.setText("")
#if QT_CONFIG(tooltip)
        self.btMax.setToolTip(QCoreApplication.translate("PyBase", u"Maximizar", None))
#endif // QT_CONFIG(tooltip)
        self.btMax.setText("")
#if QT_CONFIG(tooltip)
        self.btClose.setToolTip(QCoreApplication.translate("PyBase", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.btClose.setText("")
        self.labelDevelop.setText(QCoreApplication.translate("PyBase", u"develop", None))
        self.labelVersion.setText(QCoreApplication.translate("PyBase", u"version", None))
    # retranslateUi

