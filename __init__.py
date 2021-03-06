"""
/***************************************************************************
 MultiEdit
                                 A QGIS plugin
 MultiEdit chooses an attribute value from a vector layer and selecting the matching features, changes all the corresponding to a new value: useful if you have many features to modify.This plugin lets you write the new value in any existing field in the attribute table, for the selected features or newly created from plugin gui...
                             -------------------
        begin                : 2012-03-09
        copyright            : (C) 2018 by Giuseppe De Marco
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
 This script initializes the plugin, making it known to QGIS.
"""
from __future__ import absolute_import
def name():
    return "MultiEdit"
def description():
    return "MultiEdit chooses an attribute value from a vector layer and selecting the matching features, changes all the corresponding to a new value: useful if you have many features to modify.This plugin lets you write the new value in any existing field in the attribute table, for the selected features or newly created from plugin gui..."
def version():
    return "Version 1.1"
def icon():
    return "multiedit.png"
def qgisMinimumVersion():
    return "3.0"
def classFactory(iface):
    # load MultiEdit class from file MultiEdit
    from .multiedit import MultiEdit
    return MultiEdit(iface)
