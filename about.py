# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Mon Jul 22 18:25:49 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(810, 559)
        self.label_3 = QtGui.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(280, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(About)
        self.label.setGeometry(QtCore.QRect(220, 40, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(About)
        self.textBrowser.setGeometry(QtCore.QRect(20, 100, 761, 141))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_2 = QtGui.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 51, 51))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/MultiEdit/pienocampo.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.webView = QtWebKit.QWebView(About)
        self.webView.setGeometry(QtCore.QRect(20, 270, 771, 271))
        self.webView.setProperty("url", QtCore.QUrl(_fromUtf8("http://www.pienocampo.it/pyqgis/multiedit_help.html")))
        self.webView.setProperty("zoomFactor", 0.699999988079)
        self.webView.setObjectName(_fromUtf8("webView"))

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "Dialog", None))
        self.label_3.setText(_translate("About", "MultiEdit v 0.5", None))
        self.label.setText(_translate("About", "(c) 2013 Giuseppe De Marco\n"
" Pienocampo\n"
" www.pienocampo.it", None))
        self.textBrowser.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MultiEdit v. 0.5 August 2013 release</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Major update for Qgis 1.9 master release and API changes.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This plugins\' new releases are currently ongoing.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tips and suggestions from anyone who uses it are always welcome!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For instruction and examples valid for version 0.4 and 0.5 you can visit http://www.pienocampo.it/pyqgis/multiedit_help.html or read below!</p></body></html>", None))

from PyQt4 import QtWebKit
#import resources_rc
