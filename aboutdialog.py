from qgis.PyQt import QtCore, QtGui, QtWidgets
from .about import Ui_About
# create the dialog
class AboutDialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_About()
        self.ui.setupUi(self)


