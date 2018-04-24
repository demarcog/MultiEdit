#/***************************************************************************
# MultiEdit
# 
# MultiEdit chooses an attribute value from a vector layer and selecting the matching features, changes all the corresponding to a new value: useful if you have many features to modify.This plugin lets you write the new value in any existing field in the attribute table, for the selected features or newly created from plugin gui...
#                             -------------------
#        begin                : 2012-03-09
#        copyright            : (C) 2012 by Giuseppe De Marco
#        email                : info@pienocampo.it
# ***************************************************************************/
# 
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# Makefile for a PyQGIS plugin 

PLUGINNAME = multiedit

PY_FILES = multiedit.py multieditdialog.py aboutdialog.py __init__.py

EXTRAS = icon.png 

UI_FILES = ui_multiedit.py about.py

RESOURCE_FILES = resources.py

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc5 -o $@  $<

%.py : %.ui
	pyuic5 -o $@ $<

# The deploy  target only works on unix like operating system where
# the Python plugin directory is located at:
# $HOME/.qgis/python/plugins
deploy: compile
	mkdir -p $(HOME)/.local/share/QGIS/QGIS3/profiles/default/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/.local/share/QGIS/QGIS3/profiles/default/python/plugins/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(HOME)/.local/share/QGIS/QGIS3/profiles/default/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/.local/share/QGIS/QGIS3/profiles/default/python/plugins/$(PLUGINNAME)
	cp -vf $(EXTRAS) $(HOME)/.local/share/QGIS/QGIS3/profiles/default/python/plugins/$(PLUGINNAME)

