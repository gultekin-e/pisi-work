#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from ui/ui_scrPackage.ui on Wed Jan 16 00:44:34 2013
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_packageWidget(object):
    def setupUi(self, packageWidget):
        packageWidget.setObjectName(_fromUtf8("packageWidget"))
        packageWidget.resize(577, 505)
        packageWidget.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(packageWidget)
        self.gridLayout.setMargin(20)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBoxUpdates = QtGui.QGroupBox(packageWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxUpdates.sizePolicy().hasHeightForWidth())
        self.groupBoxUpdates.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxUpdates.setFont(font)
        self.groupBoxUpdates.setStyleSheet(_fromUtf8("#groupBoxUpdates{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(219, 219, 219, 100), stop:1 rgba(255, 255, 255, 100));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}"))
        self.groupBoxUpdates.setTitle(_fromUtf8(""))
        self.groupBoxUpdates.setFlat(True)
        self.groupBoxUpdates.setObjectName(_fromUtf8("groupBoxUpdates"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBoxUpdates)
        self.verticalLayout.setMargin(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.showTray = QtGui.QCheckBox(self.groupBoxUpdates)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        self.showTray.setFont(font)
        self.showTray.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.showTray.setObjectName(_fromUtf8("showTray"))
        self.verticalLayout.addWidget(self.showTray)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkUpdate = QtGui.QCheckBox(self.groupBoxUpdates)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        self.checkUpdate.setFont(font)
        self.checkUpdate.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.checkUpdate.setObjectName(_fromUtf8("checkUpdate"))
        self.horizontalLayout.addWidget(self.checkUpdate)
        self.updateInterval = QtGui.QSpinBox(self.groupBoxUpdates)
        self.updateInterval.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.updateInterval.setFont(font)
        self.updateInterval.setStyleSheet(_fromUtf8("color: rgb(30, 43, 51)"))
        self.updateInterval.setMinimum(1)
        self.updateInterval.setMaximum(10000)
        self.updateInterval.setProperty("value", 1)
        self.updateInterval.setObjectName(_fromUtf8("updateInterval"))
        self.horizontalLayout.addWidget(self.updateInterval)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBoxUpdates)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(packageWidget)
        self.label_4.setMinimumSize(QtCore.QSize(64, 64))
        self.label_4.setMaximumSize(QtCore.QSize(64, 64))
        self.label_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/applications-other.png")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.description = QtGui.QLabel(packageWidget)
        self.description.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setStyleSheet(_fromUtf8(""))
        self.description.setFrameShadow(QtGui.QFrame.Raised)
        self.description.setWordWrap(True)
        self.description.setIndent(10)
        self.description.setObjectName(_fromUtf8("description"))
        self.horizontalLayout_2.addWidget(self.description)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.label = QtGui.QLabel(packageWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"border: 1px solid rgba(255,255,255,50);\n"
"color:white;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;"))
        self.label.setMargin(5)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.retranslateUi(packageWidget)
        QtCore.QMetaObject.connectSlotsByName(packageWidget)

    def retranslateUi(self, packageWidget):
        packageWidget.setWindowTitle(kdecore.i18n(_fromUtf8("Packages")))
        self.showTray.setText(kdecore.i18n(_fromUtf8("Show updates in the system tray")))
        self.checkUpdate.setText(kdecore.i18n(_fromUtf8("Check updates automatically every")))
        self.updateInterval.setSuffix(kdecore.i18n(_fromUtf8(" minute(s)")))
        self.description.setText(kdecore.i18n(_fromUtf8("To install and remove programs to Pardus, use Package-Manager. Package-Manager also can automatically install the latest updates available. You can set the period for checking new updates.")))
        self.label.setText(kdecore.i18n(_fromUtf8("Updates")))

import kaptan.kaptan_rc
