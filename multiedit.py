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
        copyright            : (C) 2012-2013 by Giuseppe De Marco
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import pdb
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from multieditdialog import MultiEditDialog
from aboutdialog import AboutDialog

class MultiEdit:

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
        self.action = QAction(QIcon(":/plugins/MultiEdit/multiedit.png"),"MultiEdit", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
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
        for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if layer.type() == QgsMapLayer.VectorLayer:
                count += 1
        return count

 #choose layer to process
    def chooselayer(self):
        self.dlg.ui.chosenlayer.clear()
        self.dlg.ui.txtFeedBack.clear()
        self.dlg.ui.newvalue.clear()
        for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if layer.type() == QgsMapLayer.VectorLayer:
                self.dlg.ui.chosenlayer.addItem(layer.name())
                #update other comboboxes
                self.set_select_attributes()
                self.set_unique_value()

 #choose attribute of present layers 
    def set_select_attributes(self):
        #clear comboboxes and linedits
        self.dlg.ui.Column.clear()
        self.dlg.ui.new_field.clear()
        if self.dlg.ui.chosenlayer.currentText() != "":
            layername = self.dlg.ui.chosenlayer.currentText()
            for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
                if selectlayer.name() == layername:
                    #removed for API 2 compatibility removing counter and iteritems()
                    #for index, field in selectlayer.dataProvider().fields().iteritems():
                    for field in selectlayer.dataProvider().fields():
                        self.dlg.ui.Column.addItem(field.name())
                        self.dlg.ui.new_field.addItem(field.name())
                    #once populated combobox with fields 
                    #names populate attributes values
                    self.set_unique_value()

    
    #choose attribute value
    def select_all(self):
        self.selectall = 0
        layername = self.dlg.ui.chosenlayer.currentText()
        #select layer
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if selectlayer.name() == layername:
                selectlayer.setSelectedFeatures([])
                selectlayer.invertSelection()
                self.selectall = 1


    def set_select_value(self):
        self.dlg.ui.oldattribute.clear()
        column = self.dlg.ui.Column.currentText()
        layername = self.dlg.ui.chosenlayer.currentText()
        #output = ""
        #select layer
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if selectlayer.name() == layername:
                provider = selectlayer.dataProvider()
                #select field and fetch values
                #removed for API 2 compatibility for index, field in provider.fields().iteritems():
                for field in provider.fields():
                    if field.name() == column:
                        request = QgsFeatureRequest().setSubsetOfAttributes()
                        for f in selectlayer.getFeatures():
                            attrs = f.attributes()
                            #remove k and iteritems for api 2.0
                            #for (k,attr) in attrs.iteritems():
                            for attr in attrs:
                                if attr != None:
                                    self.dlg.ui.oldattribute.addItem(attr)
                                #output += "\n" + attr.toString()
                                #self.dlg.ui.txtFeedBack.setText(output)
 
 #find unique values in layer feature classification 
    def set_unique_value(self):
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        #uniqueprovider = None
        self.dlg.ui.oldattribute.clear()
        uniquelayer = self.dlg.ui.chosenlayer.currentText()
        uniquecolumn = self.dlg.ui.Column.currentText()
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if selectlayer.name() == uniquelayer:
                uniqueprovider = selectlayer.dataProvider()
                list = []
                if (uniqueprovider):
                    fields = uniqueprovider.fields()
                    for field in fields:
                        if field.name() == uniquecolumn:
                            id = fields.indexFromName(field.name())
                            uniquevalue = uniqueprovider.uniqueValues(id)
                            for uv in uniquevalue:
                                self.dlg.ui.oldattribute.addItem(unicode(uv))

    #Select features to process
    def select_features(self):
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        provider = None
        #clear any feature from list...
        self.selectList = []
        #let's begin
        #retrieve comboboxes data
        currlayer = self.dlg.ui.chosenlayer.currentText()
        currcolumn = self.dlg.ui.Column.currentText()
        currfeature = self.dlg.ui.oldattribute.currentText()
        #turn selected layer off to ensure selection of all features in layer
        self.turn_layer_off(currlayer)
        nsel = 0
        #select data provider and layer
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if selectlayer.name() == currlayer:
                cLayer = selectlayer
                provider = cLayer.dataProvider()
                fields = provider.fields()
                index = None
                if cLayer:
                    for field in fields:
                        if field.name() == currcolumn:
                            #version 0.5--correction-----------------------------
                            #index = fields.indexFromName(field.name())
                            #select field index--------correction from ver. 0.3
                            #idx = []
                            #idx.append(index)
                            #provider.select(idx)
                            #-------------------------correction from ver. 0.3
                            #version 0.5 correction------------------------------
                            #----------------------------------------------------
                            #navigates through the features and select those whose name
                            #corresponds to the value in combo box
                            for f in cLayer.getFeatures():
                                attrs = f.attributes()
                                for attr in attrs:
                                    if unicode(attr) == currfeature:#modified to check string instead of number 0.5
                                        self.selectList.append(f.id())
        # make the actual selection
        if self.selectList:
            cLayer.setSelectedFeatures(self.selectList)
            nsel = cLayer.selectedFeatureCount()
            
        #some info in the text browser to know what's going on
        self.dlg.ui.txtFeedBack.setText(unicode(nsel)+" Feature/s selected"+"\nin Layer--> " + cLayer.name() + "\nin Field--> " + currcolumn + "\nValue to be modified--> " + currfeature)
 
    def change_to_any(self):#change values to any column of the attribute table
        self.countchange = 0
        layername = self.dlg.ui.chosenlayer.currentText()
        val = self.get_new_value()
        col_new = self.dlg.ui.new_field.currentText()
        currfeature = self.dlg.ui.oldattribute.currentText()
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if selectlayer.name() == layername:
                layer = selectlayer
        if val == "":
            QMessageBox.warning(None, "Warning","New attribute value is empty or null \n  Please type in one!")
            return
        else:
            #initialize variables and retrieve field id and change attribute value of selected 
            #feature ids  
            nF = 0
            ncol_new = 0
            if(layer):
                layer.startEditing()
                nF = layer.selectedFeatureCount()
                fields = layer.dataProvider().fields()
                for field in fields:
                    if field.name() == col_new:
                        ncol_new = fields.indexFromName(field.name())
                #some information in the textBrowser
                self.dlg.ui.txtFeedBack.setText("Field name: " + col_new + " - Field ID " + unicode(ncol_new) + "\nNumber of Features to modify--> "+ unicode(nF))
                if nF >0:
                    fields = layer.dataProvider().fields()
                    for field in fields:
                        if field.name() == col_new:
                            #function to write to all columns
                            if self.selectall > 0:
                                idx = fields.indexFromName(field.name())#retrieve field index from name
                                for f in layer.getFeatures():
                                    attrs = f.attributes()
                                    for attr in attrs:
                                        feat = f.id()
                                        layer.changeAttributeValue(feat, idx ,val)
                                        self.countchange+=1
                            else:
                                idx = fields.indexFromName(field.name())#retrieve field index from name
                                for f in layer.getFeatures():
                                    attrs = f.attributes()
                                    for attr in attrs:
                                        if unicode(attr) == currfeature:#convert anything to string to match unique values 0.5
                                            feat = f.id()
                                            layer.changeAttributeValue(feat, idx ,val)
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
            self.dlg.ui.txtFeedBack.append("Checking field:  "+unicode(confront))
            if confront == newfieldname:
                unique = 1
            else:
                unique = 0
        return unique

 #create new field in layer table
    
    def create_new_field(self):
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        layername = self.dlg.ui.chosenlayer.currentText()
        #choose layer
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if selectlayer.name() == layername:
                layer = selectlayer
                provider = layer.dataProvider()
                fields = provider.fields()
                nF = fields.count()
                self.dlg.ui.txtFeedBack.append(unicode(nF)+"   found in layer.")
                newfieldID=nF-1
                newfieldui = self.dlg.ui.newfield.text()
                if newfieldui == (""):
                    QMessageBox.critical(None,"MutiEdit","Please provide a non null field name")
                    return
                else:
                    #newfieldname = QString(self.get_field())
                    newfieldname = self.get_field()
                    unique = 0 
                    #self.dlg.ui.txtFeedBack.append(newfieldname)
                    for field in fields:
                        confront = field.name()
                        self.dlg.ui.txtFeedBack.append("Checking field:  "+unicode(confront))
                        if confront == newfieldname:
                            unique = 1
                    self.dlg.ui.txtFeedBack.append(unicode(unique))
                    if unique == 1:
                        QMessageBox.information(None, "MultiEdit","Field name already present in layer, provide another name...")
                        return
                    else:
                        layer.startEditing()
                        #   newfieldname = QString(newfieldui)
                        
                        newfieldtype = self.dlg.ui.fieldtype.currentText()
                        self.dlg.ui.txtFeedBack.append("New Field  "+unicode(newfieldname)+" , Field Type  "+unicode(newfieldtype))
                        if newfieldtype == "Int":
                            provider.addAttributes ([QgsField(newfieldname,QVariant.Int,"Integer",10,0)])
                        if newfieldtype == "String":
                            provider.addAttributes ([QgsField(newfieldname,QVariant.String,"String",255,0)])
                        if newfieldtype == "Double":
                            provider.addAttributes ([QgsField(newfieldname,QVariant.Double, "Real", 32,2)])
                    
                layer.commitChanges()
                layer.reload()
                self.dlg.ui.newfield.clear()
        return

 #Clear selected vector features 
    def clearselection(self):
        self.dlg.ui.txtFeedBack.clear()
        clearlist = []
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if selectlayer.type() == QgsMapLayer.VectorLayer:
                selectlayer.setSelectedFeatures(clearlist)

    def show_table(self):
        #shows attribute table of chosen layer 
        table_layer=self.dlg.ui.chosenlayer.currentText()
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if selectlayer.name() == table_layer:
                show_layer_t = selectlayer
                self.iface.showAttributeTable(show_layer_t)
            
    
    def get_new_value(self):
        new_val = self.dlg.ui.newvalue.text()
        return new_val

    def turn_layer_off(self, loadedlayer):
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
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
        #put rest of the code here
        self.clearselection()

        #----version 0.4 
        #disconnect QT objects to avoid strange behaviours in create new field function
        #after exiting and reloading the plugin
        QObject.disconnect(self.dlg.ui.chosenlayer, SIGNAL("currentIndexChanged(QString)"), self.clearselection)
        QObject.disconnect(self.dlg.ui.chosenlayer, SIGNAL("currentIndexChanged(QString)"), self.clearselection)
        QObject.disconnect(self.dlg.ui.create_new_field, SIGNAL("clicked(bool)"), self.newfield_connect)
        QObject.disconnect(self.dlg.ui.select, SIGNAL("clicked(bool)"), self.select_features)
        QObject.disconnect(self.dlg.ui.all, SIGNAL("clicked(bool)"), self.select_all)
        QObject.disconnect(self.dlg.ui.unselect, SIGNAL("clicked(bool)"), self.clearselection)
        QObject.disconnect(self.dlg.ui.save, SIGNAL("clicked(bool)"), self.save_edits)
        QObject.disconnect(self.dlg.ui.show_t, SIGNAL("clicked(bool)"), self.show_table)
        QObject.disconnect(self.dlg.ui.change_another, SIGNAL("clicked(bool)"), self.change_to_any)
        QObject.disconnect(self.dlg.ui.Exit, SIGNAL("clicked(bool)"), self.exit)
        QObject.disconnect(self.dlg.ui.about, SIGNAL("clicked(bool)"), self.doabout )
        #-----version 0.4 end    
        
        #turn on layers turned off by turn_layer_off f(x) stored in a list
        #globally defined called turnedoffLayers, this method preserves the list, if one needs to purge items
        #one should use this, given a the list: while a: function(a.pop)
        #while self.turnedoffLayers:
        #   self.turn_layer_on(self.turnedoffLayers.pop)
        self.restore_visibility()
        if (self.saved == False and self.countchange > 0):
            QMessageBox.information(None,"INFO","Remember to review the changes \n and then save the edits. Thank you")
        #self.iface.zoomToPrevious()
        return

    def save_edits(self):
        self.saved = False
        #chose layer name to check in iteration
        layername = self.dlg.ui.chosenlayer.currentText()
        #browse layers in project to find matching items, select layer and if started editing
        #commit changes...
        for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
            if selectlayer.name() == layername:
                if (selectlayer.isEditable()):
                    selectlayer.commitChanges()
                    #show result in textBrowser
                    self.dlg.ui.txtFeedBack.setText("Edits saved in Layer--> "+ layername)
                    self.saved = True
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

    def unload(self):
        #compatibility with 2.0 menu
        # check if Raster/Vector menu available and remove our buttons from appropriate
        # menu and toolbar
        if hasattr(self.iface, "addPluginToVectorMenu"):
            self.iface.removePluginVectorMenu("&MultiEdit",self.action)
            self.iface.removeVectorToolBarIcon(self.action)
        else:
            self.iface.removePluginMenu("&MultiEdit",self.action)
            self.iface.removeToolBarIcon(self.action)
            
            
# run method that performs all the real work----------------------------------------------------------------------

    def run(self):
        #initial check if no vector layer no party...
        self.countchange = 0
        self.turnedoffLayers = []
        self.saved = None
        check = 0
        check = self.checkvector()
        if check == 0:
            self.iface.messageBar().pushMessage("MultiEdit","No vector layers \n Please load some, then reload plugin", level=QgsMessageBar.CRITICAL, duration=3)
            return
        else:

            boolvar ="YES"
            #Initial comboboxes filling
            self.chooselayer()
            #pyqtRemoveInputHook()
            #pdb.set_trace()
            #Connect to change in layer combobox and column combobox and execute
            #information retrieving procedures
            QObject.connect(self.dlg.ui.chosenlayer, SIGNAL("currentIndexChanged(QString)"), self.set_select_attributes)
            self.set_select_attributes()
            #every change in layer choice clears selection anyway
            QObject.connect(self.dlg.ui.chosenlayer, SIGNAL("currentIndexChanged(QString)"), self.clearselection)
            #populate attribute values combobox
            #2nd version stable with unique values
            self.set_unique_value()
            #Connection for 2nd version
            #QObject.connect(self.dlg.ui.Column, SIGNAL("currentIndexChanged(QString)"), self.set_unique_value)
            QObject.connect(self.dlg.ui.Column, SIGNAL("activated(QString)"), self.set_unique_value)#changed  
            #Connection for 1st version
            #QObject.connect(self.dlg.ui.Column, SIGNAL("currentIndexChanged(QString)"), self.set_select_value)
            #self.set_select_value()
            #Plaintext event
            QObject.connect(self.dlg.ui.newvalue, SIGNAL("textChanged(QString)"), self.get_new_value)
            #Buttons events
            QObject.connect(self.dlg.ui.select, SIGNAL("clicked(bool)"), self.select_features)
            QObject.connect(self.dlg.ui.all, SIGNAL("clicked(bool)"), self.select_all)
            QObject.connect(self.dlg.ui.unselect, SIGNAL("clicked(bool)"), self.clearselection)
            QObject.connect(self.dlg.ui.save, SIGNAL("clicked(bool)"), self.save_edits)
            QObject.connect(self.dlg.ui.show_t, SIGNAL("clicked(bool)"), self.show_table)
            QObject.connect(self.dlg.ui.create_new_field, SIGNAL("clicked(bool)"), self.newfield_connect)
            QObject.connect(self.dlg.ui.change_another, SIGNAL("clicked(bool)"), self.change_to_any)#the real thing 2...
            self.dlg.show()
            self.dlg.ui.txtFeedBack.append("VECTOR LAYER? -->"+ boolvar)
            self.dlg.ui.txtFeedBack.append("Saved layers? -->"+unicode(self.saved))
            self.dlg.ui.txtFeedBack.append("Turned off layer by MultiEdit"+unicode(self.turnedoffLayers))
            QObject.connect(self.dlg.ui.Exit, SIGNAL("clicked(bool)"), self.exit)
            #----ver 0.4
            QObject.connect(self.dlg.ui.about, SIGNAL("clicked(bool)"), self.doabout )
            #----ver 0.4 end
            

