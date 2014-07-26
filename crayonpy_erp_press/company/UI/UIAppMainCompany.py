# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIAppMainCompany.ui'
#
# Created: Tue Jul 15 21:18:58 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuCompany = QtGui.QMenu(self.menubar)
        self.menuCompany.setObjectName(_fromUtf8("menuCompany"))
        self.menuBookStore = QtGui.QMenu(self.menubar)
        self.menuBookStore.setObjectName(_fromUtf8("menuBookStore"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.menuCompany.addAction(self.action_2)
        self.menuCompany.addAction(self.action_3)
        self.menuBookStore.addAction(self.action)
        self.menubar.addAction(self.menuCompany.menuAction())
        self.menubar.addAction(self.menuBookStore.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "회사거래정보", None))
        self.menuCompany.setTitle(_translate("MainWindow", "회사정보", None))
        self.menuBookStore.setTitle(_translate("MainWindow", "발주거래처", None))
        self.menu.setTitle(_translate("MainWindow", "작가관리", None))
        self.menu_2.setTitle(_translate("MainWindow", "주문관리", None))
        self.action.setText(_translate("MainWindow", "서점", None))
        self.action_2.setText(_translate("MainWindow", "회사정보", None))
        self.action_3.setText(_translate("MainWindow", "직원정보", None))

