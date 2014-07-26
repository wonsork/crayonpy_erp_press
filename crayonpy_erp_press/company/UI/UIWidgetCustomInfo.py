# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIWidgetCustomInfo.ui'
#
# Created: Fri Jul 25 11:36:13 2014
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

class Ui_FormCustomers(object):
    def setupUi(self, FormCustomers):
        FormCustomers.setObjectName(_fromUtf8("FormCustomers"))
        FormCustomers.resize(500, 500)
        self.toolBox = QtGui.QToolBox(FormCustomers)
        self.toolBox.setGeometry(QtCore.QRect(40, 20, 641, 491))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.pageCusterInfo = QtGui.QWidget()
        self.pageCusterInfo.setGeometry(QtCore.QRect(0, 0, 641, 423))
        self.pageCusterInfo.setObjectName(_fromUtf8("pageCusterInfo"))
        self.formLayoutWidget = QtGui.QWidget(self.pageCusterInfo)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 10, 511, 381))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditBizName = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditBizName.setObjectName(_fromUtf8("lineEditBizName"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditBizName)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditBizBossName = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditBizBossName.setObjectName(_fromUtf8("lineEditBizBossName"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditBizBossName)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditBizNumber = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditBizNumber.setObjectName(_fromUtf8("lineEditBizNumber"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEditBizNumber)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditBizType = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditBizType.setObjectName(_fromUtf8("lineEditBizType"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEditBizType)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditBizAddr = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditBizAddr.setObjectName(_fromUtf8("lineEditBizAddr"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEditBizAddr)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_BizKind = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_BizKind.setObjectName(_fromUtf8("lineEdit_BizKind"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineEdit_BizKind)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_BizKind_2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_BizKind_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferUppercase)
        self.lineEdit_BizKind_2.setMaxLength(15)
        self.lineEdit_BizKind_2.setObjectName(_fromUtf8("lineEdit_BizKind_2"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.lineEdit_BizKind_2)
        self.label_17 = QtGui.QLabel(self.formLayoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_17)
        self.lineEditBizEmail = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditBizEmail.setObjectName(_fromUtf8("lineEditBizEmail"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.lineEditBizEmail)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout.setLayout(12, QtGui.QFormLayout.LabelRole, self.horizontalLayout)
        self.pushButtonSave = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pushButtonSave)
        self.toolBox.addItem(self.pageCusterInfo, _fromUtf8(""))
        self.pageCustomList = QtGui.QWidget()
        self.pageCustomList.setGeometry(QtCore.QRect(0, 0, 641, 423))
        self.pageCustomList.setObjectName(_fromUtf8("pageCustomList"))
        self.listWidget = QtGui.QListWidget(self.pageCustomList)
        self.listWidget.setGeometry(QtCore.QRect(10, -20, 581, 351))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.toolBox.addItem(self.pageCustomList, _fromUtf8(""))

        self.retranslateUi(FormCustomers)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormCustomers)

    def retranslateUi(self, FormCustomers):
        FormCustomers.setWindowTitle(_translate("FormCustomers", "Form", None))
        self.label_7.setText(_translate("FormCustomers", "고객정보", None))
        self.label.setText(_translate("FormCustomers", "사업자명  ", None))
        self.label_6.setText(_translate("FormCustomers", "성명(이름)", None))
        self.label_2.setText(_translate("FormCustomers", "사업자등록번호 ", None))
        self.label_3.setText(_translate("FormCustomers", "업태 ", None))
        self.label_4.setText(_translate("FormCustomers", "사업장 주소", None))
        self.label_5.setText(_translate("FormCustomers", "종목 ", None))
        self.label_8.setText(_translate("FormCustomers", "전화번호 (연락처)", None))
        self.label_17.setText(_translate("FormCustomers", "회사대표 이메일", None))
        self.pushButtonSave.setText(_translate("FormCustomers", "저장", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageCusterInfo), _translate("FormCustomers", "고객상세정보", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageCustomList), _translate("FormCustomers", "목록 ", None))

