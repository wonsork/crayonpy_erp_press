__author__ = 'kafka'

import sys

from PyQt4.QtGui import QMainWindow, QApplication
from PyQt4.QtCore import pyqtSignature
from PyQt4 import  QtGui

from company.UI.UIAppMainCompany import Ui_MainWindow
from CCompanyInfo import CCompanyInfo

# from main import MainView
# from queue import Queue

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # form
        self.centralWidget=QtGui.QWidget(self)
        #
        self.fCCompanyInfo = CCompanyInfo(self.centralwidget)
        #
        # self.setCentralWidget(self.uiFormComapnyInfo)
        # self.main = MainView(self.centralWidget())
        # self.queue = UI(self.centralWidget())
        # #self.setCentralWidget(self.main)
        # self.queue.hide()
        self.setCentralWidget(self.fCCompanyInfo)

        self.show()

    @pyqtSignature("")
    def on_actionMain_triggered(self):
        """
        Slot documentation goes here.
        """
        self.queue.hide()
        self.main.show()
        #self.setCentralWidget(self.main)

    @pyqtSignature("")
    def on_actionView_Queue_triggered(self):
        """
        Slot documentation goes here.
        """
        # self.main.hide()
        # self.queue.show()
        #self.setCentralWidget(self.queue)

if __name__ == "__main__":
        app = QApplication(sys.argv)
        mw = MainWindow()
        sys.exit(app.exec_())
