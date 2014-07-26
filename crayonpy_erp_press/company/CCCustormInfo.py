# -*- coding:utf-8 -*-
# COPYRIGHT CRAYONSOFTWARE EMAIL:WONSORK@GMAIL.COM
__author__ = 'kafka'


import sqlalchemy
from sqlalchemy.orm import sessionmaker
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtSql, QtGui

from database.DatabasePub import TBCompany,TBUser,DataBaseCompany
from UI.UIWidgetCustomInfo import Ui_FormCustomers






# 고객정보를 저장하고 그목록을 볼  수 있다.
class CCCustomerInfo(QMainWindow, Ui_FormCustomers):
    """
    Class documentation goes here.
    """
    def __del__(self):
        pass
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # super(Window, self).__init__(parent)
        print "...고객관리 생성"


        self.listWidget.setSortingEnabled(True)

        for item in range(1,10):
            itemWidget = QListWidgetItem(QtCore.QString("name"))
            self.listWidget.addItem(itemWidget)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWindow = QMainWindow()
    clock = CCCustomerInfo(mainWindow)
    clock.show()
    sys.exit(app.exec_())





