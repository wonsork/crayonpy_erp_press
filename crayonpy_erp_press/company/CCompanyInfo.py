# -*- coding:utf-8 -*-
__author__ = 'kafka'

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4 import QtSql, QtGui



    # self.actionOnButtonEvent.trigger=self.onEventButtonSave
    # self.actionActionOnButtonUserSave.trigger=self.onEventButtonUserSave


from database.DatabasePub import TBCompany,TBUser,DataBaseCompany
from company.UI.UIFormCompanyInfo import Ui_FormCompanyInfo


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

def toKOR(kor):
    # return  QtCore.QTextCodec.codecForName('EUC-KR').toUnicode(kor)
    return unicode(kor)

database = DataBaseCompany()
print "DataBaseCompany.DB_PATH " ,database.get_DBPATH()

def createConnection():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    # db.setDatabaseName(':memory:')
    db.setDatabaseName(database.get_DBPATH())
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                              "This example needs SQLite support. Please read "
                              "the Qt SQL driver documentation for information "
                              "how to build it.\n\n"
                              "Click Cancel to exit."),
                QtGui.QMessageBox.Cancel)
        return False
    return True




class CustomSqlModel(QtSql.QSqlQueryModel):
    def data(self, index, role):
        value = super(CustomSqlModel, self).data(index, role)
        # if value is not None and role == QtCore.Qt.DisplayRole:
        #     if index.column() == 0:
        #         return '#%d' % value
        #     elif index.column() == 2:
        #         return value

        if role == QtCore.Qt.TextColorRole and index.column() == 1:
            return QtGui.QColor(QtCore.Qt.blue)

        return value



def initializeModel(model):
    # model.setTable('tbuser')
    model.setQuery('select id,userEmail,userName,userMinNumber,userPhone,userAddr,userEtc from tbuser')
    #
    # model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)

    #
    # userEmail  =Column(String(50),nullable=False,unique=True)#이메일이 곧 아이디다.
    # userName=Column(String(10)) #이름.
    # userMinNumber=Column(String(20)) #주민등록번호...
    # userPhone=Column(String(20)) #핸드폰.
    # userPosition=Column(String(10))#직책
    # userAddr=Column(String(50)) #집주소.
    # userEtc = Column(String(255)) #기타사항..
    model.setHeaderData(0, QtCore.Qt.Horizontal, "key")
    model.setHeaderData(1, QtCore.Qt.Horizontal, _fromUtf8("Email"))
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Name")
    model.setHeaderData(3, QtCore.Qt.Horizontal, "MinNumber")
    model.setHeaderData(4, QtCore.Qt.Horizontal, "Phone")
    model.setHeaderData(5, QtCore.Qt.Horizontal, "Address")
    model.setHeaderData(6, QtCore.Qt.Horizontal, "Etc")
    # model.setHeaderData(6, QtCore.Qt.Horizontal, "userMinNumber")



class CCompanyInfo(QMainWindow, Ui_FormCompanyInfo):


    """
    Class documentation goes here.
    """
    def __del__(self):
        self.session.close()

    def __init__(self, parent = None):
        """
        Constructor
        """
        self.tbUser=None
        self.tbCompany=None

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # set triiger...



        print ".....Create cc company info"

        print sqlalchemy.__version__
        self.show()

        databaseCompany = DataBaseCompany()
        engine = databaseCompany.onCreate()
        print "create engine value ", engine
        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()


        self.doBindUITBCompanInfo()


    def doBindUITBCompanInfo(self):

        companys = self.session.query(TBCompany).all()
        print "company " , companys
        for company in companys:
            self.tbCompany = company

        users = self.session.query(TBUser).all()


        for user in users:
            print "user value ", user

        createConnection()
        self.model = CustomSqlModel()
        initializeModel(self.model)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        self.tableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self.tableView))

		# self.tableView.horizontalHeader().setStretchLastSection(True)
		# self.tableView.resizeColumnsToContents()
        self.tableView.selectionModel().selectionChanged.connect(self.onSelectionChanged)
        self.tableView.pressed.connect(self.onSelectItem)
        # self.tableView.selectionModel().selec
        # self.theSelectionModel = self.tableView.selectionModel()
        self.connect(self.model, QtCore.SIGNAL("selectionChanged()"), self.getSelection)

    def onSelectItem(self, index):
        print "Sel onSelectItem ",index
        # userinfo = index
        # print "userinfo.Email ", index.takeFirst()
        # print "QModelIndex.row()",index.row()
        # print "QModelIndex.internalId()",index.internalId()
        # print "QModelIndex.model() ", index.model().data()
        # print "QModelIndex.column() ", index.column()
        # # QItemSelection.takeFirst()
        # print "QModelIndex.data() ", index.data(0).toString()

    def onSelectionChanged(self, *args):
        print "Sel onSelectionChanged ",args[0]
        item = args[0];
        print "QItemSelection.first() ", item.indexes()

        for sell in item.indexes():
            print sell.data(0).toString()
        # QItemSelection.indexes()
        # print "userinfo.userName ", args.userName
        """
        Called when the ranks view selection changes.
        """
        # self.applyIf()

    def getSelection(self):
		print "getSelection() ..."
		# index = self.theSelectionModel.currentIndex()
		# print "index: ", index

    # userEmail  =Column(String(50),nullable=False,unique=True)#이메일이 곧 아이디다.
    # userName=Column(String(10)) #이름.
    # userMinNumber=Column(String(20)) #주민등록번호...
    # userPhone=Column(String(20)) #핸드폰.
    # userPosition=Column(String(10))#직책
    # userAddr=Column(String(50)) #집주소.
    # userEtc = Column(String(255)) #기타사항..









    # self.actionOnButtonEvent.trigger=self.onEventButtonSave
    # self.actionActionOnButtonUserSave.trigger=self.onEventButtonUserSave
    # self.tabWidget.blockSignals(True) #just for not showing the initial message
    # self.tabWidget.currentChanged.connect(self.onTabChanged) #changed!

    # #@pyqtSlot()
    # def onTabChanged(self,index):
    #
    #
    # # def onChange(self,i): #changed!
    #     QtGui.QMessageBox.information(self,
    #               "Tab Index Changed!",
    #               "Current Tab Index: %d" % index ) #changed!

    def onEventButtonSave(self):
        print "FUCK SAVE button click"

        abizName = self.lineEditBizName.text()
        abossName = self.lineEditBizBossName.text()
        abizType = self.lineEditBizType.text()
        abizKind = self.lineEdit_BizKind.text()
        abizAddr = self.lineEditBizAddr.text()
        aBizCode= self.lineEditBizNumber.text()
        abizEmail=self.lineEditBizEmail.text()

        # abizEmail = self.lineedit
        abizName = toKOR(abizName)
        abossName = toKOR(abossName)
        abizType = toKOR(abizType)
        abizKind = toKOR(abizKind)
        abizEmail = toKOR(abizEmail)
        abizAddr = toKOR(abizAddr)
        aBizCode = toKOR(aBizCode)
        print "bizName ", abizName
        print "abossName " , abossName


        try :
            self.tbCompany = TBCompany(bizName=abizName,bizCode=aBizCode,bizBossName=abossName,bizType=abizType
                               ,bizKind=abizKind,bizEmail=abizEmail,bizAddr=abizAddr)
            self.session.add(self.tbCompany)
            self.session.commit()

        except (ValueError, ZeroDivisionError,Exception):
            print "err "
            self.session.close()
            databaseCompany = DataBaseCompany()
            engine = databaseCompany.onCreate()
            Session = sessionmaker()
            Session.configure(bind=engine)
            self.session = Session()
        else:
            print "else"


        our_user = self.session.query(TBCompany).all()
        print "all " , our_user


    def onEventButtonUserSave(self):
        print "...call 사용자 저장 및 입력..."
        aUserEmail = self.lineEditUserEmail.text()
        aUserName = self.lineEditUserName.text()
        aUserMinNum = self.lineEditMinNumber.text()
        aUserPhone = self.lineEditUserPhone.text()
        aUserPosition = self.lineEditUserPosition.text()
        aUserAddr = self.lineEditUserAddr.text()
        aUserEtc = self.lineEditUserEtc.text()

        aUserEmail = toKOR(aUserEmail)
        aUserName = toKOR(aUserName)
        aUserMinNum = toKOR(aUserMinNum)
        aUserPhone = toKOR(aUserPhone)
        aUserPosition = toKOR(aUserPosition)
        aUserAddr = toKOR(aUserAddr)
        aUserEtc = toKOR(aUserEtc)


        try:
            self.tbUser = TBUser(userEmail=aUserEmail,userName=aUserName,userMinNumber=aUserMinNum,userPhone=aUserPhone,userPosition=aUserPosition,
                            userAddr=aUserAddr,userEtc = aUserEtc,companykey=self.tbCompany.id)
            self.session.add(self.tbUser)
            self.session.commit()

        except (NameError,Exception):
            print "err "

            self.session.close()
            databaseCompany = DataBaseCompany()
            engine = databaseCompany.onCreate()
            Session = sessionmaker()
            Session.configure(bind=engine)
            self.session = Session()



        users = self.session.query(TBUser).all()
        print "all " , users

        createConnection()
        self.model = CustomSqlModel()
        initializeModel(self.model)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        # self.tableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self.tableView))

		# self.tableView.horizontalHeader().setStretchLastSection(True)
		# self.tableView.resizeColumnsToContents()
        self.tableView.selectionModel().selectionChanged.connect(self.onSelectionChanged)
        self.tableView.pressed.connect(self.onSelectItem)
        # self.tableView.selectionModel().selec
        # self.theSelectionModel = self.tableView.selectionModel()
        self.connect(self.model, QtCore.SIGNAL("selectionChanged()"), self.getSelection)


