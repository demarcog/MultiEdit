# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_multiedit.ui'
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

class Ui_MultiEdit(object):
    def setupUi(self, MultiEdit):
        MultiEdit.setObjectName(_fromUtf8("MultiEdit"))
        MultiEdit.resize(801, 517)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        MultiEdit.setFont(font)
        self.chosenlayer = QtGui.QComboBox(MultiEdit)
        self.chosenlayer.setGeometry(QtCore.QRect(10, 80, 261, 27))
        self.chosenlayer.setObjectName(_fromUtf8("chosenlayer"))
        self.label = QtGui.QLabel(MultiEdit)
        self.label.setGeometry(QtCore.QRect(20, 60, 67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.Column = QtGui.QComboBox(MultiEdit)
        self.Column.setGeometry(QtCore.QRect(10, 139, 261, 27))
        self.Column.setObjectName(_fromUtf8("Column"))
        self.label_2 = QtGui.QLabel(MultiEdit)
        self.label_2.setGeometry(QtCore.QRect(20, 119, 67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.oldattribute = QtGui.QComboBox(MultiEdit)
        self.oldattribute.setGeometry(QtCore.QRect(10, 200, 261, 27))
        self.oldattribute.setObjectName(_fromUtf8("oldattribute"))
        self.label_3 = QtGui.QLabel(MultiEdit)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 141, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(MultiEdit)
        self.label_4.setGeometry(QtCore.QRect(300, 180, 161, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtFeedBack = QtGui.QTextBrowser(MultiEdit)
        self.txtFeedBack.setGeometry(QtCore.QRect(10, 360, 781, 131))
        self.txtFeedBack.setObjectName(_fromUtf8("txtFeedBack"))
        self.line = QtGui.QFrame(MultiEdit)
        self.line.setGeometry(QtCore.QRect(10, 50, 841, 20))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_5 = QtGui.QLabel(MultiEdit)
        self.label_5.setGeometry(QtCore.QRect(60, 0, 681, 51))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.select = QtGui.QPushButton(MultiEdit)
        self.select.setGeometry(QtCore.QRect(20, 249, 111, 41))
        self.select.setObjectName(_fromUtf8("select"))
        self.unselect = QtGui.QPushButton(MultiEdit)
        self.unselect.setGeometry(QtCore.QRect(140, 249, 121, 41))
        self.unselect.setObjectName(_fromUtf8("unselect"))
        self.change_another = QtGui.QPushButton(MultiEdit)
        self.change_another.setGeometry(QtCore.QRect(440, 250, 171, 41))
        self.change_another.setObjectName(_fromUtf8("change_another"))
        self.new_field = QtGui.QComboBox(MultiEdit)
        self.new_field.setGeometry(QtCore.QRect(293, 80, 261, 27))
        self.new_field.setObjectName(_fromUtf8("new_field"))
        self.label_6 = QtGui.QLabel(MultiEdit)
        self.label_6.setGeometry(QtCore.QRect(293, 59, 261, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(MultiEdit)
        self.label_7.setGeometry(QtCore.QRect(10, 343, 67, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.Exit = QtGui.QPushButton(MultiEdit)
        self.Exit.setGeometry(QtCore.QRect(620, 310, 171, 41))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.save = QtGui.QPushButton(MultiEdit)
        self.save.setGeometry(QtCore.QRect(617, 250, 171, 41))
        self.save.setObjectName(_fromUtf8("save"))
        self.show_t = QtGui.QPushButton(MultiEdit)
        self.show_t.setGeometry(QtCore.QRect(440, 310, 171, 41))
        self.show_t.setObjectName(_fromUtf8("show_t"))
        self.fieldtype = QtGui.QComboBox(MultiEdit)
        self.fieldtype.setGeometry(QtCore.QRect(577, 138, 71, 27))
        self.fieldtype.setObjectName(_fromUtf8("fieldtype"))
        self.fieldtype.addItem(_fromUtf8(""))
        self.fieldtype.addItem(_fromUtf8(""))
        self.fieldtype.addItem(_fromUtf8(""))
        self.create_new_field = QtGui.QPushButton(MultiEdit)
        self.create_new_field.setGeometry(QtCore.QRect(650, 138, 141, 27))
        self.create_new_field.setObjectName(_fromUtf8("create_new_field"))
        self.line_6 = QtGui.QFrame(MultiEdit)
        self.line_6.setGeometry(QtCore.QRect(3, 290, 791, 20))
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_8 = QtGui.QLabel(MultiEdit)
        self.label_8.setGeometry(QtCore.QRect(584, 60, 201, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_10 = QtGui.QLabel(MultiEdit)
        self.label_10.setGeometry(QtCore.QRect(580, 120, 161, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.newvalue = QtGui.QLineEdit(MultiEdit)
        self.newvalue.setGeometry(QtCore.QRect(296, 201, 491, 27))
        self.newvalue.setObjectName(_fromUtf8("newvalue"))
        self.newfield = QtGui.QLineEdit(MultiEdit)
        self.newfield.setGeometry(QtCore.QRect(574, 80, 220, 27))
        self.newfield.setObjectName(_fromUtf8("newfield"))
        self.label_12 = QtGui.QLabel(MultiEdit)
        self.label_12.setGeometry(QtCore.QRect(220, 10, 51, 51))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/MultiEdit/pienocampo.png")))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.line_3 = QtGui.QFrame(MultiEdit)
        self.line_3.setGeometry(QtCore.QRect(270, 60, 20, 241))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_2 = QtGui.QFrame(MultiEdit)
        self.line_2.setGeometry(QtCore.QRect(560, 60, 20, 111))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_4 = QtGui.QFrame(MultiEdit)
        self.line_4.setGeometry(QtCore.QRect(570, 166, 221, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.about = QtGui.QPushButton(MultiEdit)
        self.about.setGeometry(QtCore.QRect(610, 10, 171, 41))
        self.about.setObjectName(_fromUtf8("about"))

        self.retranslateUi(MultiEdit)
        QtCore.QObject.connect(self.Exit, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), MultiEdit.reject)
        QtCore.QMetaObject.connectSlotsByName(MultiEdit)

    def retranslateUi(self, MultiEdit):
        MultiEdit.setWindowTitle(_translate("MultiEdit", "MultiEdit", None))
        self.label.setText(_translate("MultiEdit", "Layer", None))
        self.label_2.setText(_translate("MultiEdit", "Field", None))
        self.label_3.setText(_translate("MultiEdit", "Old Attribute value", None))
        self.label_4.setText(_translate("MultiEdit", "New Attribute value", None))
        self.label_5.setText(_translate("MultiEdit", "MultiEdit 0.5  \n"
"(C) 2013 by Giuseppe De Marco\n"
" www.pienocampo.it", None))
        self.select.setText(_translate("MultiEdit", "Select\n"
"Features", None))
        self.unselect.setText(_translate("MultiEdit", "Clear Selected\n"
"Features", None))
        self.change_another.setText(_translate("MultiEdit", "Write value \n"
" to chosen field", None))
        self.label_6.setText(_translate("MultiEdit", "Field to write the new value to:", None))
        self.label_7.setText(_translate("MultiEdit", "Output", None))
        self.Exit.setText(_translate("MultiEdit", "Exit", None))
        self.save.setText(_translate("MultiEdit", "Save Changes", None))
        self.show_t.setText(_translate("MultiEdit", "Show Attribute Table \n"
"of selected Layer", None))
        self.fieldtype.setItemText(0, _translate("MultiEdit", "String", None))
        self.fieldtype.setItemText(1, _translate("MultiEdit", "Int", None))
        self.fieldtype.setItemText(2, _translate("MultiEdit", "Double", None))
        self.create_new_field.setText(_translate("MultiEdit", "Create new Field", None))
        self.label_8.setText(_translate("MultiEdit", "Create Field (Optional)", None))
        self.label_10.setText(_translate("MultiEdit", "Field type", None))
        self.about.setText(_translate("MultiEdit", "About/Help", None))

#import resources_rc
