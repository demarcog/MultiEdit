"""
/***************************************************************************
 MultiEditDialog
                                 A QGIS plugin
 MultiEdit chooses an attribute value from a vector layer and selecting the matching features, changes all the corresponding to a new value: useful if you have many features to modify.This plugin lets you write the new value in any existing field in the attribute table, for the selected features or newly created from plugin gui...
                             -------------------
        begin                : 2012-03-09
        copyright            : (C) 2012 by Giuseppe De Marco
        email                : info@pienocampo.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_multiedit import Ui_MultiEdit
# create the dialog for zoom to point
class MultiEditDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MultiEdit()
        self.ui.setupUi(self)
