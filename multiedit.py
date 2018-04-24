"""
/***************************************************************************
 MultiEdit
                                 A QGIS plugin
 MultiEdit chooses an attribute value from a vector layer and selecting the
 matching features, changes all the corresponding to a new value: useful if 
 you have many features to modify.This plugin lets you write the new value 
 in any existing field in the attribute table, for the selected features or 
 newly created from plugin gui...
                              -------------------
        begin                : 2012-03-09
        copyright            : (C) 2012-2015 by Giuseppe De Marco
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
from __future__ import absolute_import
from builtins import str
from builtins import range
from builtins import object
# Import the PyQt and QGIS libraries
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtXml import *
from qgis.core import *
import pdb
# Initialize Qt resources from file resources.py
from . import resources
# Import the code for the dialog
from .multieditdialog import MultiEditDialog
#from .Ui_About import Ui_About
from .aboutdialog import AboutDialog

class MultiEdit(object):

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # create our GUI dialog
        self.dlg = MultiEditDialog()
        self.dlga = AboutDialog()
        #initialization for select features
        self.turnedoffLayers = []
        self.selectList = []
        self.cLayer = None
        self.provider = None
        self.saved = False
        self.countchange = 0
        selectall = 0
        
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/MultiEdit/multiedit.png"),u"MultiEdit", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)
        #compatibility with 2.0 menu
        # check if Raster/Vector menu available
        if hasattr(self.iface, "addPluginToVectorMenu"):
            # Raster menu and toolbar available
            self.iface.addPluginToVectorMenu("&Pienocampo", self.action)
            self.iface.addVectorToolBarIcon(self.action)
        else:
            # there is no Raster/Vector menu, place plugin under Plugins menu as usual
            self.iface.addToolBarIcon(self.action)
            self.iface.addPluginToMenu("&Pienocampo", self.action)
                    
                
#Custom functions begin-------------------------------------------------------


 #checks if layer are vector type
    def checkvector(self):
        count = 0
        for name, layer in list(QgsProject.instance().mapLayers().items()):
            if layer.type() == QgsMapLayer.VectorLayer:
                count += 1
        return count

 #choose layer to process
    def chooselayer(self):
        #layerlist=[]
        #slist=[]
        self.dlg.ui.txtFeedBack.clear()
        self.dlg.ui.newvalue.clear()
        #update other comboboxes
        self.set_select_attributes()
        self.set_unique_value()

 #choose attribute of present layers 
    def set_select_attributes(self):
        #clear comboboxes and linedits
        #self.dlg.ui.Column.clear()
#        self.dlg.ui.new_field.clear()
        if self.dlg.ui.chosenlayer.currentLayer():
            layer = self.dlg.ui.chosenlayer.currentLayer()
            self.dlg.ui.Column.setLayer(layer)
            self.dlg.ui.new_field.setLayer(layer)
            self.set_unique_value()

    
    #choose attribute value
    def select_all(self):
        self.selectall = 0
        layername = self.dlg.ui.chosenlayer.currentLayer().name()
        #select layer
        for name, layer in list(QgsProject.instance().mapLayers().items()):
            if layer.name() == layername:
                layer.selectAll()
                self.selectall = 1


    def set_select_value(self):
        self.dlg.ui.oldattribute.clear()
        column = self.dlg.ui.Column.currentField()
        layername = self.dlg.ui.chosenlayer.currentLayer().name()
        #output = ""
        #select layer
        for name, layer in list(QgsProject.instance().mapLayers().items()):
            if layer.name() == layername:
                provider = layer.dataProvider()
                #select field and fetch values
                for field in provider.fields():
                    if field.name() == column:
                        request = QgsFeatureRequest().setSubsetOfAttributes()
                        for f in layer.getFeatures():
                            attrs = f.attributes()
                            for attr in attrs:
                                if attr != None:
                                    self.dlg.ui.oldattribute.addItem(attr)

 
 #find unique values in layer feature classification 
    def set_unique_value(self):
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        self.dlg.ui.oldattribute.clear()
        uniquelayer = self.dlg.ui.chosenlayer.currentLayer()
        uniquecolumn = self.dlg.ui.Column.currentField()
        for name, layer in list(QgsProject.instance().mapLayers().items()):
            if layer.name() == uniquelayer.name():
                uniqueprovider = layer.dataProvider()
                #list = []
                if (uniqueprovider):
                    fields = uniqueprovider.fields()
                    for field in fields:
                        if field.name() == uniquecolumn:
                            id = fields.indexFromName(field.name())
                            uniquevalues = uniqueprovider.uniqueValues(id)
                            for uv in uniquevalues:
                                self.dlg.ui.oldattribute.addItem(str(uv))

    #Select features to process
    def select_features(self):
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        provider = None
        #clear any feature from list...
        self.selectList = []
        #let's begin
        #retrieve comboboxes data
        currlayer = self.dlg.ui.chosenlayer.currentLayer()
        currcolumn = self.dlg.ui.Column.currentField()
        currfeature = self.dlg.ui.oldattribute.currentText()
        #turn selected layer off to ensure selection of all features in layer
        #self.turn_layer_off(currlayer)
        nsel = 0
        #select data provider and layer
        for name, layer in list(QgsProject.instance().mapLayers().items()):
            if layer == currlayer:
                cLayer = layer
                provider = layer.dataProvider()
                fields = provider.fields()
                index = None
                if layer:
                    for field in fields:
                        if field.name() == currcolumn:
                            #navigates through the features and select those whose name
                            #corresponds to the value in combo box
                            for f in layer.getFeatures():
                                attrs = f.attributes()
                                for attr in attrs:
                                    if str(attr) == currfeature:#check string instead of number
                                        self.selectList.append(f.id())
        # make the actual selection
        if self.selectList and cLayer:
            cLayer.select(self.selectList)
            nsel = cLayer.selectedFeatureCount()
            #some info in the text browser to know what's going on
            self.dlg.ui.txtFeedBack.setText(str(nsel)+" Feature/s selected"+"\nin Layer--> " + cLayer.name() + "\nin Field--> " + currcolumn + "\nValue to be modified--> " + currfeature)
 
    def change_to_any(self):#change values to any fields at the corresponding row attribute
        self.countchange = 0
        anylayer = self.dlg.ui.chosenlayer.currentLayer()
        val = self.get_new_value()
        col_new = self.dlg.ui.new_field.currentText()
        currfeature = self.dlg.ui.oldattribute.currentText()
        for name, layer in list(QgsProject.instance().mapLayers().items()):
            if layer == anylayer:
                selectlayer = layer
        if val == "":
            QMessageBox.warning(None, "Warning","New attribute value is empty or null \n  Please type in one!")
            return
        else:
            #initialize variables and retrieve field id and change attribute value of selected 
            #feature ids  
            nF = 0
            ncol_new = 0
            if(selectlayer):
                selectlayer.startEditing()
                nF = selectlayer.selectedFeatureCount()
                fields = selectlayer.dataProvider().fields()
                for field in fields:
                    if field.name() == col_new:
                        ncol_new = fields.indexFromName(field.name())
                #some information in the textBrowser
                self.dlg.ui.txtFeedBack.setText("Field name: " + col_new + " - Field ID " + str(ncol_new) + "\nNumber of Features to modify--> "+ str(nF) +"\nValue to be written--> "+ str(val))
                if nF >0:
                    fields = selectlayer.dataProvider().fields()
                    for field in fields:
                        if field.name() == col_new:
                            #write the value to all the rows in a field 
                            if self.selectall > 0:
                                idx = fields.indexFromName(field.name())#retrieve field index from name
                                for f in selectlayer.getFeatures():
                                    attrs = f.attributes()
                                    for attr in attrs:
                                        feat = f.id()
                                        selectlayer.changeAttributeValue(feat, idx ,val)
                                        self.countchange+=1
                            else:
                                idx = fields.indexFromName(field.name())#retrieve field index from name
                                for f in selectlayer.getFeatures():
                                    attrs = f.attributes()
                                    for attr in attrs:
                                        #write the value to only matching old attribute value of a field 
                                        if str(attr) == currfeature:#convert anything to unicode string to match unique values 0.5
                                            feat = f.id()
                                            selectlayer.changeAttributeValue(feat, idx ,val)
                                            self.countchange+=1
                else:
                    QMessageBox.critical(None,"Error", "Please select at least one feature from current layer")
            else:
                QMessageBox.critical(None,"Error","Please select a layer")
        return self.countchange

    def get_field(self):
        Name = self.dlg.ui.newfield.text()
        return Name
    
    def check_unique_fields(self, fields, newfieldname):
        for i in fields:
            confront = fields[i].name()
            self.dlg.ui.txtFeedBack.append("Searching fields for:  "+str(confront))
            if confront == newfieldname:
                unique = 1
            else:
                unique = 0
        return unique

    def create_new_field(self):
        #create new field in layer table
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        layername = self.dlg.ui.chosenlayer.currentLayer()
        #choose layer
        for name, selectlayer in list(QgsProject.instance().mapLayers().items()):
            if selectlayer.name() == layername:
                layer = selectlayer
                provider = layer.dataProvider()
                fields = provider.fields()
                nF = fields.count()
                self.dlg.ui.txtFeedBack.append(str(nF)+" fields found in layer.")
                #used to start from 0
                newfieldID=nF-1
                newfieldui = self.dlg.ui.newfield.text()
                if newfieldui == (""):
                    QMessageBox.critical(None,"MutiEdit","Please provide a non null field name")
                    return
                else:
                    newfieldname = self.get_field()
                    unique = 0 
                    for field in fields:
                        confront = field.name()
                        self.dlg.ui.txtFeedBack.append("Searching fields names for:  "+str(confront))
                        if confront == newfieldname:
                            unique = 1
                    if unique == 1:
                        QMessageBox.information(None, "MultiEdit","Field name already present in layer, provide another name...")
                        return
                    else:
                        layer.startEditing()
                        newfieldtype = self.dlg.ui.fieldtype.currentText()
                        self.dlg.ui.txtFeedBack.append("Creating new field: "+str(newfieldname)+" , Type  "+str(newfieldtype))
                        if newfieldtype == "Int":
                            provider.addAttributes ([QgsField(newfieldname,QVariant.Int,"Integer",10,0)])
                        if newfieldtype == "String":
                            provider.addAttributes ([QgsField(newfieldname,QVariant.String,"String",255,0)])
                        if newfieldtype == "Double":
                            provider.addAttributes ([QgsField(newfieldname,QVariant.Double, "Real", 32,2)])
                layer.commitChanges()
                layer.reload()
                #self.dlg.ui.newfield.clear()
        return

 #Clear selected vector features 
    def clearselection(self):
        self.dlg.ui.txtFeedBack.clear()
        for name, layer in list(QgsProject.instance().mapLayers().items()):
            if layer.type() == QgsMapLayer.VectorLayer:
                layer.removeSelection()

    def show_table(self):
        #shows attribute table of chosen layer 
        table_layer=self.dlg.ui.chosenlayer.currentLayer()
        if table_layer:
            for name, layer in list(QgsProject.instance().mapLayers().items()):
                if layer == table_layer:
                    #show_layer_t = layer
                    self.iface.showAttributeTable(layer)
            
    
    def get_new_value(self):
        new_val = self.dlg.ui.newvalue.text()
        return new_val

    def turn_layer_off(self, loadedlayer):
        for name, selectlayer in list(QgsProject.instance().mapLayers().items()):
            if selectlayer.name() == loadedlayer:
                theloadedlayer = selectlayer
                legend = self.iface.legendInterface()
                #access legendInteface class to determine if a layer is visible
                #then set it unvisible and add layer to a list
                if (legend.isLayerVisible(theloadedlayer)):
                    legend.setLayerVisible(theloadedlayer, False)
                    self.turnedoffLayers.append(selectlayer)
        
    def turn_layer_on (self, unloadedlayer):
        #access legendInterface class and turn unloadelayer layer on
        legend = self.iface.legendInterface()
        legend.setLayerVisible(unloadedlayer, True)

    def restore_visibility(self):
        #pick turned off layers from a list and set them visible
        if self.turnedoffLayers != []:
            for i in range(len(self.turnedoffLayers)):
                self.turn_layer_on(self.turnedoffLayers[i])
        else:
            return

    def exit(self):
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        self.clearselection()
        #disconnect QT objects 
        self.dlg.ui.chosenlayer.currentIndexChanged.disconnect(self.clearselection)
        self.dlg.ui.create_new_field.clicked.disconnect(self.newfield_connect)
        self.dlg.ui.select.clicked.disconnect(self.select_features)
        self.dlg.ui.all.clicked.disconnect(self.select_all)
        self.dlg.ui.unselect.clicked.disconnect(self.clearselection)
        self.dlg.ui.save.clicked.disconnect(self.save_edits)
        self.dlg.ui.show_t.clicked.disconnect(self.show_table)
        self.dlg.ui.change_another.clicked.disconnect(self.change_to_any)
        self.dlg.ui.Exit.clicked.disconnect(self.exit)
        self.dlg.ui.about.clicked.disconnect(self.doabout)
        #turn on layers turned off by turn_layer_off
        self.restore_visibility()
        if (self.saved == False and self.countchange > 0):
            self.iface.messageBar().pushMessage("MultiEdit","Remember to review the changes and then save the edits. Thank you", level=Qgis.Info)
        return

    def save_edits(self):
        self.saved = False
        #chose layer name to check in iteration
        layername = self.dlg.ui.chosenlayer.currentLayer()
        #browse layers in project to find matching items, select layer and if started editing
        #commit changes...
        for name, selectlayer in list(QgsProject.instance().mapLayers().items()):
            if selectlayer.name() == layername:
                if (selectlayer.isEditable()):
                    selectlayer.commitChanges()
                    #show result in textBrowser
                    self.dlg.ui.txtFeedBack.setText("Edits saved in Layer--> "+ layername)
                    self.saved = True
                    #check for unsaved layers set to 0...
                    self.countchange = 0
        #update comboboxes
        self.set_unique_value()
                    
        return self.saved
    
    def newfield_connect(self):
        self.create_new_field()
        self.set_select_attributes()
        return

    def doabout(self):
        self.dlga.show()

#Custom function end-------------------------------------------------------------------------------------------------------------------

    def unload(self):#to remove <2.0 compatibility!!!
        #compatibility with 2.0 menu
        # check if Raster/Vector menu is available and remove buttons from appropriate
        # menu and toolbar
        if hasattr(self.iface, "addPluginToVectorMenu"):
            self.iface.removePluginVectorMenu("&Pienocampo",self.action)
            self.iface.removeVectorToolBarIcon(self.action)
        else:
            self.iface.removePluginMenu("&Pienocampo",self.action)
            self.iface.removeToolBarIcon(self.action)
            
            
# run method that performs all the real work----------------------------------------------------------------------

    def run(self):
        #initial check if no vector layer no party...
        self.countchange = 0
        self.turnedoffLayers = []
        self.saved = None
        self.selectall = 0
        check = 0
        check = self.checkvector()
        if check == 0:
            self.iface.messageBar().pushMessage("MultiEdit","No vector layers \n Please load some, then reload plugin", level=Qgis.Critical, duration=3)
            return
        else:
            boolvar ="YES"
            #Initial comboboxes filling
            self.chooselayer()
            #pyqtRemoveInputHook()
            #pdb.set_trace()
            #Connect to change in layer combobox and column combobox and execute
            #information retrieving procedures
            self.dlg.ui.chosenlayer.currentIndexChanged.connect(self.set_select_attributes)
            self.set_select_attributes()
            #every change in layer choice clears selection anyway
            self.dlg.ui.chosenlayer.currentIndexChanged.connect(self.clearselection)
            #populate attribute values combobox
            #2nd version stable with unique values
            self.set_unique_value()
            #Connection for 2nd version
            #QObject.connect(self.dlg.ui.Column, SIGNAL("currentIndexChanged(QString)"), self.set_unique_value)
            self.dlg.ui.Column.activated.connect(self.set_unique_value)#changed  
            #Connection for 1st version
            #QObject.connect(self.dlg.ui.Column, SIGNAL("currentIndexChanged(QString)"), self.set_select_value)
            #self.set_select_value()
            #Plaintext event
            self.dlg.ui.newvalue.textChanged.connect(self.get_new_value)
            #Buttons events
            self.dlg.ui.select.clicked.connect(self.select_features)
            self.dlg.ui.all.clicked.connect(self.select_all)
            self.dlg.ui.unselect.clicked.connect(self.clearselection)
            self.dlg.ui.save.clicked.connect(self.save_edits)
            self.dlg.ui.show_t.clicked.connect(self.show_table)
            self.dlg.ui.create_new_field.clicked.connect(self.newfield_connect)
            self.dlg.ui.change_another.clicked.connect(self.change_to_any)#the real thing 2...
            self.dlg.show()
            self.dlg.ui.txtFeedBack.append("VECTOR LAYER? -->"+ boolvar)
            self.dlg.ui.txtFeedBack.append("Saved layers? -->"+str(self.saved))
            self.dlg.ui.txtFeedBack.append("Turned off layer by MultiEdit"+str(self.turnedoffLayers))
            self.dlg.ui.Exit.clicked.connect(self.exit)
            #----About dialog
            self.dlg.ui.about.clicked.connect(self.doabout)

