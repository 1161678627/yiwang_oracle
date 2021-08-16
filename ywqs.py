# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ywqs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(358, 167)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 81, 31))
        self.label.setFont(font)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(90, 20, 121, 31))
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"background-color: rgb(218, 218, 218);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 81, 31))
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 80, 121, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 40, 111, 41))
        self.pushButton.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 125, 321, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_3.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"+++", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7ed1\u5b9a\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5145\u503c\u91d1\u989d", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u5145\u503c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u63d0\u793a\uff1a\u5145\u503c\u91d1\u989d\u4ec5\u652f\u630120\uff0c50\uff0c100\u4e09\u79cd\u8f93\u5165", None))
    # retranslateUi

