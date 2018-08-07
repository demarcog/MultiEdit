# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(810, 559)
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(280, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(220, 40, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(About)
        self.textBrowser.setGeometry(QtCore.QRect(20, 100, 761, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 51, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/plugins/MultiEdit/pienocampo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.webView = QtWebKitWidgets.QWebView(About)
        self.webView.setGeometry(QtCore.QRect(10, 250, 771, 271))
        self.webView.setUrl(QtCore.QUrl("qrc:/plugins/MultiEdit/singlehtml/singlehtml/index.html"))
        self.webView.setZoomFactor(0.699999988079071)
        self.webView.setObjectName("webView")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Dialog"))
        self.label_3.setText(_translate("About", "MultiEdit v 1.1"))
        self.label.setText(_translate("About", "(c) 2018 Giuseppe De Marco\n"
" d2gis\n"
" www.d2gis.com"))
        self.textBrowser.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MultiEdit v. 1.1 April 2018 release</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Major updates for Qgis 3.x release and API changes. Added function to select all features and change values for all by the new Select all pushbutton. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This plugins\' new releases are currently ongoing.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

from PyQt5 import QtWebKitWidgets
#import resources_rc
