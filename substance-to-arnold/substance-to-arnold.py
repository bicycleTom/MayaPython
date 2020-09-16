from PySide2 import QtCore
from PySide2 import QtWidgets
import maya.cmds as cmds
import os
import os.path
import re



PLUGIN_NAME         = 'Substance Painter 2019 to Autodesk Maya 2019 Arnold 5'
PLUGIN_VERSION      = '1.1'
## Orignal Code by Mostafa Samir
## Updated by Calvert 
## https://github.com/calvertcreates/substance-to-arnold

class SubstanceImporter():
    def __init__(self):
        print(PLUGIN_NAME +' ver '+ PLUGIN_VERSION + '\n')
        
        
        self.initUI()
        
    def initUI(self):
        #Create our main window
        self.dlgMain = QtWidgets.QDialog()
        self.dlgMain.setWindowTitle(PLUGIN_NAME +'ver'+ PLUGIN_VERSION)
        self.dlgMain.setFixedSize(220,450)
        self.dlgMain.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)




        
        
        #Create vertical layout
        self.layVDlgMain = QtWidgets.QVBoxLayout()
        self.dlgMain.setLayout(self.layVDlgMain)
        self.dlgMain.setStyleSheet ("""QWidget {background-color:#1c2122;border-width: 2px;border-color: #0d5666;border-style: solid;border-radius: 4; }QPushButton {color: white;background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #056, stop: 1 #99e, stop: 1.49 #027, stop: 0.5 #66b, stop: 1 #77c);border-width: 2px;border-color: #22d8ff;border-style: solid;border-radius: 4;padding: 3px;font-size: 12px;padding-left: 5px;padding-right: 5px;min-width: 50px;max-width: 175px;min-height: 13px;max-height: 23px;}QGroupBox { background-color: #141c58; border-radius: 4;border:2px solid #0d5666;}""");

        
        #Create Dirctory Group box
        self.grpBrowseForDirectory = QtWidgets.QGroupBox('Texture Directory')
        self.layVDlgMain.addWidget(self.grpBrowseForDirectory)

        
                     
        
        #Create H layout in Dirctory Group box
        self.layHBrowseForDirectory = QtWidgets.QHBoxLayout()
        self.grpBrowseForDirectory.setLayout(self.layHBrowseForDirectory)
        
        #Create Push btn for browse Dirctory  in Group box
        self.btnBrowseForDir = QtWidgets.QPushButton('Select Texture Directory')
        self.layHBrowseForDirectory.addWidget(self.btnBrowseForDir)
        self.btnBrowseForDir.clicked.connect(self.btnBrowseForDirClicked)
        
        
        #Create Texture Slot Group box
        self.grpTexSlot = QtWidgets.QGroupBox('TextureSlots')
        self.layVDlgMain.addWidget(self.grpTexSlot)
        
        
        #Create V layout for texture slots
        self.layVTexSlot = QtWidgets.QVBoxLayout()
        self.grpTexSlot.setLayout(self.layVTexSlot)
        
        
        
        #Create H layout for BaseColor slot
        self.layHBaseColorSlot = QtWidgets.QHBoxLayout()
        self.layVTexSlot.addLayout(self.layHBaseColorSlot)
        
        #Create CheckBoxs for BaseColor slot
        self.chbaseifuseSlot = QtWidgets.QCheckBox('BaseColor  ')
        self.layHBaseColorSlot.addWidget(self.chbaseifuseSlot)
        self.chbaseifuseSlot.stateChanged.connect(self.chbaseifuseSlotState)
                    
        #Create Line edit
        self.lineBaseColorSlot = QtWidgets.QLineEdit()
        self.layHBaseColorSlot.addWidget(self.lineBaseColorSlot)
        self.lineBaseColorSlot.setText('BaseColor')
        self.lineBaseColorSlot.setDisabled(1)
        
        #Create H layout for Metalness slot
        self.layHMetalnessSlot = QtWidgets.QHBoxLayout()
        self.layVTexSlot.addLayout(self.layHMetalnessSlot)
        
        #Create CheckBoxs for Metalness slot
        self.chMetalnessSlot = QtWidgets.QCheckBox('Metalness  ')
        self.layHMetalnessSlot.addWidget(self.chMetalnessSlot)
        self.chMetalnessSlot.stateChanged.connect(self.chMetalnessSlotState)
                    
        #Create Line edit
        self.lineMetalnessSlot = QtWidgets.QLineEdit()
        self.layHMetalnessSlot.addWidget(self.lineMetalnessSlot)
        self.lineMetalnessSlot.setText('Metalness')
        self.lineMetalnessSlot.setDisabled(1)
        
        
         #Create H layout for Roughness slot
        self.layHRoughnessSlot = QtWidgets.QHBoxLayout()
        self.layVTexSlot.addLayout(self.layHRoughnessSlot)
        
        #Create CheckBoxs for Roughness slot
        self.chRoughnessSlot = QtWidgets.QCheckBox('Roughness')
        self.layHRoughnessSlot.addWidget(self.chRoughnessSlot)
        self.chRoughnessSlot.stateChanged.connect(self.chRoughnessSlotState)
                    
        #Create Line edit
        self.lineRoughnesSlot = QtWidgets.QLineEdit()
        self.layHRoughnessSlot.addWidget(self.lineRoughnesSlot)
        self.lineRoughnesSlot.setText('Roughness')
        self.lineRoughnesSlot.setDisabled(1)       


        #Create H layout for Bump slot
        self.layHBumpSlot = QtWidgets.QHBoxLayout()
        self.layVTexSlot.addLayout(self.layHBumpSlot)

        #Create H layout for Normal slot
        self.layHNormalSlot = QtWidgets.QHBoxLayout()
        self.layVTexSlot.addLayout(self.layHNormalSlot)
        
        #Create CheckBoxs for Normal slot
        self.chkNormalSlot = QtWidgets.QCheckBox('Normal       ')
        self.layHNormalSlot.addWidget(self.chkNormalSlot)
        self.chkNormalSlot.stateChanged.connect(self.chkNormalSlotState)
                    
        #Create Line edit
        self.lineNormalSlot = QtWidgets.QLineEdit()
        self.layHNormalSlot.addWidget(self.lineNormalSlot)
        self.lineNormalSlot.setText('Normal')
        self.lineNormalSlot.setDisabled(1)
        
        #Create H layout for Emission slot
        self.layHEmissionSlot = QtWidgets.QHBoxLayout()
        self.layVTexSlot.addLayout(self.layHEmissionSlot)
        
        #Create CheckBoxs for Emission slot
        self.chkEmissionSlot = QtWidgets.QCheckBox('Emission    ')
        self.layHEmissionSlot.addWidget(self.chkEmissionSlot)
        self.chkEmissionSlot.stateChanged.connect(self.chkEmissionSlotState)
                    
        #Create Line edit
        self.lineEmissionSlot = QtWidgets.QLineEdit()
        self.layHEmissionSlot.addWidget(self.lineEmissionSlot)
        self.lineEmissionSlot.setText('Emissive')
        self.lineEmissionSlot.setDisabled(1)

        #Create H layout for Height slot
        self.layHHeightSlot = QtWidgets.QHBoxLayout()
        self.layVTexSlot.addLayout(self.layHHeightSlot)
        
        #Create CheckBoxs for Height slot
        self.chkHeightSlot = QtWidgets.QCheckBox('Height       ')
        self.layHHeightSlot.addWidget(self.chkHeightSlot)
        self.chkHeightSlot.stateChanged.connect(self.chkHeightSlotState)
                    
        #Create Line edit
        self.lineHeightSlot = QtWidgets.QLineEdit()
        self.layHHeightSlot.addWidget(self.lineHeightSlot)
        self.lineHeightSlot.setText('Height')
        self.lineHeightSlot.setDisabled(1)        
        
        #Create groupbox for extention
        self.grpTextureExtension = QtWidgets.QGroupBox('Texture Info')
        self.layVDlgMain.addWidget(self.grpTextureExtension)
        
        #Create layout for texture extension
        self.layVTextureExtention = QtWidgets.QVBoxLayout()
        self.grpTextureExtension.setLayout(self.layVTextureExtention)
        
        self.layHTextureExtention = QtWidgets.QHBoxLayout()
        self.layVTextureExtention.addLayout(self.layHTextureExtention)
        
        #add combobox for file extenstions
        self.comboBoxTexEx = QtWidgets.QComboBox()
        self.layHTextureExtention.addWidget(self.comboBoxTexEx) 
        
        #Create List for texture extension which avaiable in substance
        texExtensionCombo = ['ALL','.png','.bmp','.ico','.jpg','.jng','.pbm','.pbmraw','.pgm','.mgmraw','.ppm','.ppmraw','.tga','.tiff','.tif','.wbmp','.xpm','.gif','.hdr','.exr','.j2k','.jp2','.pfm','.webp','.jpeg-xr','.psd']
        self.comboBoxTexEx.addItems(texExtensionCombo)
        
        
        self.layHTextureTiles = QtWidgets.QHBoxLayout()
        self.layVTextureExtention.addLayout(self.layHTextureTiles)
        
      
        #Create checkbox for UDIM
        self.udimCheckBox = QtWidgets.QCheckBox('UDIM')
        self.layHTextureTiles.addWidget(self.udimCheckBox)
        self.udimCheckBox.stateChanged.connect(self.stateUdimCheckBox)
        
     
        #add btn for select the model
        self.btnUdim = QtWidgets.QPushButton('Exported Model')
        self.layHTextureTiles.addWidget(self.btnUdim)
        self.btnUdim.setEnabled(0)
        self.btnUdim.clicked.connect(self.btnUdimSignal)
        
    
        #Create Import Group box
        self.grpImport = QtWidgets.QGroupBox('Material')
        self.layVDlgMain.addWidget(self.grpImport)
        
        #Create H Layout
        self.layHImport = QtWidgets.QHBoxLayout()
        self.grpImport.setLayout(self.layHImport)
       
       
        #Create Import Button
        self.btnImportTex = QtWidgets.QPushButton('Create materials')
        self.layHImport.addWidget(self.btnImportTex)
        self.btnImportTex.setEnabled(0)
        self.btnImportTex.clicked.connect(self.btnImportTexClicked)

       
        
        self.dlgMain.show()        
            
    def btnBrowseForDirClicked(self):
        self.ImportTexDir = QtWidgets.QFileDialog.getExistingDirectory()
        self.btnBrowseForDir.setText(self.ImportTexDir)
        if (self.ImportTexDir == None):
            print('Please,Select Your Texture Export Path')
            
        else:
            self.btnImportTex.setEnabled(not self.btnImportTex.isEnabled())


     
    def chbaseifuseSlotState(self):
        self.lineBaseColorSlot.setEnabled(not self.lineBaseColorSlot.isEnabled())

    def chRoughnessSlotState(self):
        self.lineRoughnesSlot.setEnabled(not self.lineRoughnesSlot.isEnabled())

    def chkNormalSlotState(self):
        self.lineNormalSlot.setEnabled(not self.lineNormalSlot.isEnabled()) 

    def chkEmissionSlotState(self):
        self.lineEmissionSlot.setEnabled(not self.lineEmissionSlot.isEnabled())         

    def chMetalnessSlotState(self):
        self.lineMetalnessSlot.setEnabled(not self.lineMetalnessSlot.isEnabled())

    def chkHeightSlotState(self):
        self.lineHeightSlot.setEnabled(not self.lineHeightSlot.isEnabled())     
     
    def stateUdimCheckBox(self):
        self.btnUdim.setEnabled(not self.btnUdim.isEnabled())
        
    def btnUdimSignal(self):
        self.modelNameWithPath = QtWidgets.QFileDialog.getOpenFileName() 
        self.btnUdim.setText(os.path.basename(self.modelNameWithPath[0]))
        
    def btnImportTexClicked(self):
        self.arnoldImport()
        
    def searchForString(self,search,string):
        myNewString = string.replace('_',' ')
        resultAsWord  = re.findall('\\b'+search +'\\b',myNewString)
        
        if (resultAsWord):
            return True
        
        else:
            return False
        
        
        
    
    def arnoldImport(self):
        sel                  = cmds.ls(selection =True)
        path                = self.ImportTexDir
        fileExtention   = self.comboBoxTexEx.currentText()
        if (fileExtention   == "ALL"):
			fileExtention   = ""
			
        
		
        paramtersList   = []
        
        
        
        
        dicSlotsChkBoxs = {'baseColor':self.chbaseifuseSlot.isChecked(),'metalness':self.chMetalnessSlot.isChecked()
                            ,'specularRoughness':self.chRoughnessSlot.isChecked(),'Height':self.chkHeightSlot.isChecked(),
                            'normalCamera':self.chkNormalSlot.isChecked(),'emissionColor':self.chkEmissionSlot.isChecked()}
        
        
        dictexNameUserInput = {'baseColor':self.lineBaseColorSlot.text(),'metalness':self.lineMetalnessSlot.text()
                            ,'specularRoughness':self.lineRoughnesSlot.text(),'Height':self.lineHeightSlot.text(),
                            'normalCamera':self.lineNormalSlot.text(),'emissionColor':self.lineEmissionSlot.text()}
        
        for i in range(0,len(dicSlotsChkBoxs)):
            if (dicSlotsChkBoxs.values()[i] == True):
                paramtersList.append(dicSlotsChkBoxs.keys()[i])
                

       
        
        for i in range(0,len(sel)):                 
            shaderType       = cmds.nodeType(sel[i], i=True)
            shadingGroup    = cmds.listConnections(sel[i],type='shadingEngine')
            selLoop             = sel[i]
            shaderName = cmds.listConnections (shadingGroup[0] + ".surfaceShader")
            
            
            if(shaderType[1] == 'aiStandardSurface'):   
                #scan all files in path
                for file in os.listdir(path):
                    
                    if (self.udimCheckBox.isChecked() == True):
                        modelName       = os.path.basename(self.modelNameWithPath[0])
                        #Search for udim
                        #print(os.path.splitext(modelName)[0],file)
                        if (-1 < file.find('1001') and self.searchForString(os.path.splitext(modelName)[0], file)):
                            #print(os.path.splitext(modelName)[0], file)
                            
                           #search if the file ends with the correct extension or not
                            if(file.endswith(fileExtention)):
                                #search for the material slots paramaters
                                for i in range(0,len(paramtersList)):
                                    #if paramaters found in dic take user input
                                    if(paramtersList[i] in dictexNameUserInput):
                                        texName             = dictexNameUserInput.get(paramtersList[i])
                                        #search for user names input in the texture it self
                                        if(-1 < file.find(texName)):
                                            texFullName = path +'/' + file
                                            print(texFullName + 'found')
                                       
                                            #Create t7exture node and make default connections
                                            fileNode      = cmds.shadingNode('file',asTexture = True,isColorManaged =True,name = 'Tex_'+ selLoop +'_'+ paramtersList[i])
                                            placeTex     = cmds.shadingNode('place2dTexture',asTexture = True)
                                            

                                            cmds.connectAttr(placeTex + '.outUV',fileNode + '.uvCoord')
                                            cmds.connectAttr(placeTex + '.uvFilterSize',fileNode + '.uvFilterSize')
                                            cmds.connectAttr(placeTex + '.coverage',fileNode + '.coverage')
                                            cmds.connectAttr(placeTex + '.translateFrame',fileNode + '.translateFrame')
                                            cmds.connectAttr(placeTex + '.rotateFrame',fileNode + '.rotateFrame')
                                            cmds.connectAttr(placeTex + '.mirrorU',fileNode + '.mirrorU')
                                            cmds.connectAttr(placeTex + '.mirrorV',fileNode + '.mirrorV')
                                            cmds.connectAttr(placeTex + '.stagger',fileNode + '.stagger')
                                            cmds.connectAttr(placeTex + '.wrapU',fileNode + '.wrapU')
                                            cmds.connectAttr(placeTex + '.wrapV',fileNode + '.wrapV')
                                            cmds.connectAttr(placeTex + '.repeatUV',fileNode + '.repeatUV')
                                            cmds.connectAttr(placeTex + '.offset',fileNode + '.offset')
                                            cmds.connectAttr(placeTex + '.rotateUV',fileNode + '.rotateUV')
                                            cmds.connectAttr(placeTex + '.noiseUV',fileNode + '.noiseUV')
                                            cmds.connectAttr(placeTex + '.vertexUvOne',fileNode + '.vertexUvOne')
                                            cmds.connectAttr(placeTex + '.vertexUvTwo',fileNode + '.vertexUvTwo')
                                            cmds.connectAttr(placeTex + '.vertexUvThree',fileNode + '.vertexUvThree')
                                            cmds.connectAttr(placeTex + '.vertexCameraOne',fileNode + '.vertexCameraOne')
                                            
                                            #set texture node path 
                                            cmds.setAttr(fileNode+'.fileTextureName',texFullName,type='string') 
                                            cmds.setAttr(fileNode+'.uvTilingMode',3) 
                                            
                                            
                                            
                                             
                                                
                                                
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance                                         
                                            if(paramtersList[i] == 'specularRoughness'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop +'.'+paramtersList[i]) 
                                            
                                            #if slot is baseColor plug it in to the shader
                                            elif(paramtersList[i] == 'baseColor'):
                                                cmds.setAttr(selLoop+'.base' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                            
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance    
                                            elif(paramtersList[i] == 'metalness'):
                                                cmds.setAttr(selLoop+'.metalness' ,1)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop + '.' +paramtersList[i] )
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string') 
                                            
                                            #if slot is emission plug it in to the shader    
                                            elif(paramtersList[i] == 'emissionColor'):
                                                cmds.setAttr(selLoop+'.emission' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                                
                                            #if slot is Normal plug it in to the shader
                                            #set color space to raw
                                            #change to Tangent Space Normals
                                            #uncheck  flip r and flip g
                                            elif(paramtersList[i] == 'normalCamera'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                bmpNode = cmds.shadingNode( 'bump2d', asUtility=True)
                                                cmds.setAttr(bmpNode + '.aiFlipR',0)
                                                cmds.setAttr(bmpNode + '.aiFlipG',0)
                                                cmds.setAttr(bmpNode + '.bumpInterp',1)
                                                cmds.connectAttr(fileNode + '.outAlpha',bmpNode + '.bumpValue') 
                                                cmds.connectAttr(bmpNode + '.outNormal',selLoop +'.'+paramtersList[i])

                                            #if slot is Height plug it in to the shaderGroup
                                            #set color space to raw
                                            #set alpha is Luminance
                                            elif(paramtersList[i] == 'Height'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                dispNode = cmds.shadingNode( 'displacementShader', asUtility=True)
                                                cmds.connectAttr(fileNode + '.outAlpha',dispNode + '.displacement') 
                                                cmds.connectAttr(dispNode + '.displacement',shadingGroup[0] +'.displacementShader')                                                 
                                                
                                            #if it's anyslot except above connect it directly  
                                            else:
                                                cmds.connectAttr(fileNode + '.outColor',selLoop +'.'+paramtersList[i]) 
                        
                        else:
                            print('UDIM not found in' + file)
                        
                        
                        
                    else:
                        
                        if (self.searchForString(shadingGroup[0], file)):
                           #search if the file ends with the correct extension or not
                            if(file.endswith(fileExtention)):
                                #search for the material slots paramaters
                                for i in range(0,len(paramtersList)):
                                    #if paramaters found in dic take user input
                                    if(paramtersList[i] in dictexNameUserInput):
                                        texName             = dictexNameUserInput.get(paramtersList[i])
                                        print(texName)
                                        #search for user names input in the texture it self
                                        if(-1 < file.find(texName)):
                                            #print(path)
                                            texFullName = path +'/' + file
                                            print(texFullName  + 'found')
                                       
                                            #Create t7exture node and make default connections
                                            fileNode      = cmds.shadingNode('file',asTexture = True,isColorManaged =True,name = 'Tex_'+ selLoop +'_'+ paramtersList[i])
                                            placeTex     = cmds.shadingNode('place2dTexture',asTexture = True)
                                            

                                            cmds.connectAttr(placeTex + '.outUV',fileNode + '.uvCoord')
                                            cmds.connectAttr(placeTex + '.uvFilterSize',fileNode + '.uvFilterSize')
                                            cmds.connectAttr(placeTex + '.coverage',fileNode + '.coverage')
                                            cmds.connectAttr(placeTex + '.translateFrame',fileNode + '.translateFrame')
                                            cmds.connectAttr(placeTex + '.rotateFrame',fileNode + '.rotateFrame')
                                            cmds.connectAttr(placeTex + '.mirrorU',fileNode + '.mirrorU')
                                            cmds.connectAttr(placeTex + '.mirrorV',fileNode + '.mirrorV')
                                            cmds.connectAttr(placeTex + '.stagger',fileNode + '.stagger')
                                            cmds.connectAttr(placeTex + '.wrapU',fileNode + '.wrapU')
                                            cmds.connectAttr(placeTex + '.wrapV',fileNode + '.wrapV')
                                            cmds.connectAttr(placeTex + '.repeatUV',fileNode + '.repeatUV')
                                            cmds.connectAttr(placeTex + '.offset',fileNode + '.offset')
                                            cmds.connectAttr(placeTex + '.rotateUV',fileNode + '.rotateUV')
                                            cmds.connectAttr(placeTex + '.noiseUV',fileNode + '.noiseUV')
                                            cmds.connectAttr(placeTex + '.vertexUvOne',fileNode + '.vertexUvOne')
                                            cmds.connectAttr(placeTex + '.vertexUvTwo',fileNode + '.vertexUvTwo')
                                            cmds.connectAttr(placeTex + '.vertexUvThree',fileNode + '.vertexUvThree')
                                            cmds.connectAttr(placeTex + '.vertexCameraOne',fileNode + '.vertexCameraOne')
                                            
                                            #set texture node path 
                                            cmds.setAttr(fileNode+'.fileTextureName',texFullName,type='string') 
                                            
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance                                         
                                            if(paramtersList[i] == 'specularRoughness'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop +'.'+paramtersList[i]) 
                                            
                                            #if slot is baseColor plug it in to the shader
                                            elif(paramtersList[i] == 'baseColor'):
                                                cmds.setAttr(selLoop+'.base' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                            
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance    
                                            elif(paramtersList[i] == 'metalness'):
                                                cmds.setAttr(selLoop+'.metalness' ,1)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop + '.' +paramtersList[i] )
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string') 
                                            
                                            #if slot is emission plug it in to the shader    
                                            elif(paramtersList[i] == 'emissionColor'):
                                                cmds.setAttr(selLoop+'.emission' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                                
                                            #if slot is Normal plug it in to the shader
                                            #set color space to raw
                                            #change to Tangent Space Normals
                                            #uncheck  flip r and flip g
                                            elif(paramtersList[i] == 'normalCamera'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                bmpNode = cmds.shadingNode( 'bump2d', asUtility=True)
                                                cmds.setAttr(bmpNode + '.aiFlipR',0)
                                                cmds.setAttr(bmpNode + '.aiFlipG',0)
                                                cmds.setAttr(bmpNode + '.bumpInterp',1)
                                                cmds.connectAttr(fileNode + '.outAlpha',bmpNode + '.bumpValue') 
                                                cmds.connectAttr(bmpNode + '.outNormal',selLoop +'.'+paramtersList[i])

                                            #if slot is Height plug it in to the shaderGroup
                                            #set color space to raw
                                            #set alpha is Luminance
                                            elif(paramtersList[i] == 'Height'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                dispNode = cmds.shadingNode( 'displacementShader', asUtility=True)
                                                cmds.connectAttr(fileNode + '.outAlpha',dispNode + '.displacement') 
                                                cmds.connectAttr(dispNode + '.displacement',shadingGroup[0] +'.displacementShader')                                                 
                                                
                                            #if it's anyslot except above connect it directly  
                                            else:
                                                cmds.connectAttr(fileNode + '.outColor',selLoop +'.'+paramtersList[i]) 

                        else:
                            print('Cannot find '+shadingGroup[0]+' in ' + file)
                        
                        if (self.searchForString(shaderName[0], file)):
                           #search if the file ends with the correct extension or not
                            if(file.endswith(fileExtention)):
                                #search for the material slots paramaters
                                for i in range(0,len(paramtersList)):
                                    #if paramaters found in dic take user input
                                    if(paramtersList[i] in dictexNameUserInput):
                                        texName             = dictexNameUserInput.get(paramtersList[i])
                                        print(texName)
                                        #search for user names input in the texture it self
                                        if(-1 < file.find(texName)):
                                            #print(path)
                                            texFullName = path +'/' + file
                                            print(texFullName  + 'found')
                                       
                                            #Create t7exture node and make default connections
                                            fileNode      = cmds.shadingNode('file',asTexture = True,isColorManaged =True,name = 'Tex_'+ selLoop +'_'+ paramtersList[i])
                                            placeTex     = cmds.shadingNode('place2dTexture',asTexture = True)
                                            

                                            cmds.connectAttr(placeTex + '.outUV',fileNode + '.uvCoord')
                                            cmds.connectAttr(placeTex + '.uvFilterSize',fileNode + '.uvFilterSize')
                                            cmds.connectAttr(placeTex + '.coverage',fileNode + '.coverage')
                                            cmds.connectAttr(placeTex + '.translateFrame',fileNode + '.translateFrame')
                                            cmds.connectAttr(placeTex + '.rotateFrame',fileNode + '.rotateFrame')
                                            cmds.connectAttr(placeTex + '.mirrorU',fileNode + '.mirrorU')
                                            cmds.connectAttr(placeTex + '.mirrorV',fileNode + '.mirrorV')
                                            cmds.connectAttr(placeTex + '.stagger',fileNode + '.stagger')
                                            cmds.connectAttr(placeTex + '.wrapU',fileNode + '.wrapU')
                                            cmds.connectAttr(placeTex + '.wrapV',fileNode + '.wrapV')
                                            cmds.connectAttr(placeTex + '.repeatUV',fileNode + '.repeatUV')
                                            cmds.connectAttr(placeTex + '.offset',fileNode + '.offset')
                                            cmds.connectAttr(placeTex + '.rotateUV',fileNode + '.rotateUV')
                                            cmds.connectAttr(placeTex + '.noiseUV',fileNode + '.noiseUV')
                                            cmds.connectAttr(placeTex + '.vertexUvOne',fileNode + '.vertexUvOne')
                                            cmds.connectAttr(placeTex + '.vertexUvTwo',fileNode + '.vertexUvTwo')
                                            cmds.connectAttr(placeTex + '.vertexUvThree',fileNode + '.vertexUvThree')
                                            cmds.connectAttr(placeTex + '.vertexCameraOne',fileNode + '.vertexCameraOne')
                                            
                                            #set texture node path 
                                            cmds.setAttr(fileNode+'.fileTextureName',texFullName,type='string') 
                                            
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance                                         
                                            if(paramtersList[i] == 'specularRoughness'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop +'.'+paramtersList[i]) 
                                            
                                            #if slot is baseColor plug it in to the shader
                                            elif(paramtersList[i] == 'baseColor'):
                                                cmds.setAttr(selLoop+'.base' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                            
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance    
                                            elif(paramtersList[i] == 'metalness'):
                                                cmds.setAttr(selLoop+'.metalness' ,1)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop + '.' +paramtersList[i] )
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string') 
                                            
                                            #if slot is emission plug it in to the shader    
                                            elif(paramtersList[i] == 'emissionColor'):
                                                cmds.setAttr(selLoop+'.emission' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                                
                                            #if slot is Normal plug it in to the shader
                                            #set color space to raw
                                            #change to Tangent Space Normals
                                            #uncheck  flip r and flip g
                                            elif(paramtersList[i] == 'normalCamera'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                bmpNode = cmds.shadingNode( 'bump2d', asUtility=True)
                                                cmds.setAttr(bmpNode + '.aiFlipR',0)
                                                cmds.setAttr(bmpNode + '.aiFlipG',0)
                                                cmds.setAttr(bmpNode + '.bumpInterp',1)
                                                cmds.connectAttr(fileNode + '.outAlpha',bmpNode + '.bumpValue') 
                                                cmds.connectAttr(bmpNode + '.outNormal',selLoop +'.'+paramtersList[i])

                                            #if slot is Height plug it in to the shaderGroup
                                            #set color space to raw
                                            #set alpha is Luminance
                                            elif(paramtersList[i] == 'Height'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                dispNode = cmds.shadingNode( 'displacementShader', asUtility=True)
                                                cmds.connectAttr(fileNode + '.outAlpha',dispNode + '.displacement') 
                                                cmds.connectAttr(dispNode + '.displacement',shadingGroup[0] +'.displacementShader')                                                 
                                                
                                            #if it's anyslot except above connect it directly  
                                            else:
                                                cmds.connectAttr(fileNode + '.outColor',selLoop +'.'+paramtersList[i]) 

                        else:
                            print('Cannot find '+shaderName[0]+' in ' + file)



                                                
            else:
                #check the connections of the old material and delete it        
                cmds.delete(sel[i])
                #Creare new material
                materialNode = cmds.shadingNode('aiStandardSurface',asShader = True,name = sel[i])
                cmds.connectAttr(materialNode + '.outColor',shadingGroup[0] + '.surfaceShader')
                newShaderName = cmds.listConnections (shadingGroup[0] + ".surfaceShader")
                for file in os.listdir(path):
                    
                    if (self.udimCheckBox.isChecked() == True):
                        modelName       = os.path.basename(self.modelNameWithPath[0])
                        #Search for udim
                        #print(os.path.splitext(modelName)[0],file)
                        if (-1 < file.find('1001') and self.searchForString(os.path.splitext(modelName)[0], file)):
                            #print(os.path.splitext(modelName)[0], file)                            
                           #search if the file ends with the correct extension or not
                            if(file.endswith(fileExtention)):
                                #search for the material slots paramaters
                                for i in range(0,len(paramtersList)):
                                    #if paramaters found in dic take user input
                                    if(paramtersList[i] in dictexNameUserInput):
                                        texName             = dictexNameUserInput.get(paramtersList[i])
                                        #search for user names input in the texture it self
                                        if(-1 < file.find(texName)):
                                            texFullName = path +'/' + file
                                            print(texFullName + 'found')
                                       
                                            #Create t7exture node and make default connections
                                            fileNode      = cmds.shadingNode('file',asTexture = True, isColorManaged =True,name = 'Tex_'+ materialNode +'_'+ paramtersList[i])
                                            placeTex     = cmds.shadingNode('place2dTexture',asTexture = True)
                                            

                                            cmds.connectAttr(placeTex + '.outUV',fileNode + '.uvCoord')
                                            cmds.connectAttr(placeTex + '.uvFilterSize',fileNode + '.uvFilterSize')
                                            cmds.connectAttr(placeTex + '.coverage',fileNode + '.coverage')
                                            cmds.connectAttr(placeTex + '.translateFrame',fileNode + '.translateFrame')
                                            cmds.connectAttr(placeTex + '.rotateFrame',fileNode + '.rotateFrame')
                                            cmds.connectAttr(placeTex + '.mirrorU',fileNode + '.mirrorU')
                                            cmds.connectAttr(placeTex + '.mirrorV',fileNode + '.mirrorV')
                                            cmds.connectAttr(placeTex + '.stagger',fileNode + '.stagger')
                                            cmds.connectAttr(placeTex + '.wrapU',fileNode + '.wrapU')
                                            cmds.connectAttr(placeTex + '.wrapV',fileNode + '.wrapV')
                                            cmds.connectAttr(placeTex + '.repeatUV',fileNode + '.repeatUV')
                                            cmds.connectAttr(placeTex + '.offset',fileNode + '.offset')
                                            cmds.connectAttr(placeTex + '.rotateUV',fileNode + '.rotateUV')
                                            cmds.connectAttr(placeTex + '.noiseUV',fileNode + '.noiseUV')
                                            cmds.connectAttr(placeTex + '.vertexUvOne',fileNode + '.vertexUvOne')
                                            cmds.connectAttr(placeTex + '.vertexUvTwo',fileNode + '.vertexUvTwo')
                                            cmds.connectAttr(placeTex + '.vertexUvThree',fileNode + '.vertexUvThree')
                                            cmds.connectAttr(placeTex + '.vertexCameraOne',fileNode + '.vertexCameraOne')
                                            
                                            #set texture node path 
                                            cmds.setAttr(fileNode+'.fileTextureName',texFullName,type='string') 
                                            cmds.setAttr(fileNode+'.uvTilingMode',3) 
                                            
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance                                         
                                            if(paramtersList[i] == 'specularRoughness'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop +'.'+paramtersList[i]) 
                                            
                                            #if slot is baseColor plug it in to the shader
                                            elif(paramtersList[i] == 'baseColor'):
                                                cmds.setAttr(selLoop+'.base' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                            
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance    
                                            elif(paramtersList[i] == 'metalness'):
                                                cmds.setAttr(selLoop+'.metalness' ,1)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop + '.' +paramtersList[i] )
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string') 
                                            
                                            #if slot is emission plug it in to the shader    
                                            elif(paramtersList[i] == 'emissionColor'):
                                                cmds.setAttr(selLoop+'.emission' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                                
                                            #if slot is Normal plug it in to the shader
                                            #set color space to raw
                                            #change to Tangent Space Normals
                                            #uncheck  flip r and flip g
                                            elif(paramtersList[i] == 'normalCamera'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                bmpNode = cmds.shadingNode( 'bump2d', asUtility=True)
                                                cmds.setAttr(bmpNode + '.aiFlipR',0)
                                                cmds.setAttr(bmpNode + '.aiFlipG',0)
                                                cmds.setAttr(bmpNode + '.bumpInterp',1)
                                                cmds.connectAttr(fileNode + '.outAlpha',bmpNode + '.bumpValue') 
                                                cmds.connectAttr(bmpNode + '.outNormal',selLoop +'.'+paramtersList[i])

                                            #if slot is Height plug it in to the shaderGroup
                                            #set color space to raw
                                            #set alpha is Luminance
                                            elif(paramtersList[i] == 'Height'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                dispNode = cmds.shadingNode( 'displacementShader', asUtility=True)
                                                cmds.connectAttr(fileNode + '.outAlpha',dispNode + '.displacement') 
                                                cmds.connectAttr(dispNode + '.displacement',shadingGroup[0] +'.displacementShader')                                                 
                                                
                                            #if it's anyslot except above connect it directly  
                                            else:
                                                cmds.connectAttr(fileNode + '.outColor',selLoop +'.'+paramtersList[i]) 
                        
                        else:
                            print('UDIM not found in ' + file)
                        
                        
                    else:
                        
                        if (self.searchForString(newShaderName[0], file)):                            
                           #search if the file ends with the correct extension or not
                            if(file.endswith(fileExtention)):
                                #search for the material slots paramaters
                                for i in range(0,len(paramtersList)):
                                    #if paramaters found in dic take user input
                                    if(paramtersList[i] in dictexNameUserInput):
                                        texName             = dictexNameUserInput.get(paramtersList[i])
                                        print(texName)
                                        #search for user names input in the texture it self
                                        if(-1 < file.find(texName)):
                                            texFullName = path +'/' + file
                                            print(texFullName + 'found')
                                       
                                            #Create t7exture node and make default connections
                                            fileNode      = cmds.shadingNode('file',asTexture = True, isColorManaged =True , name = 'Tex_'+ materialNode +'_'+ paramtersList[i])
                                            placeTex     = cmds.shadingNode('place2dTexture',asTexture = True)
                                            

                                            cmds.connectAttr(placeTex + '.outUV',fileNode + '.uvCoord')
                                            cmds.connectAttr(placeTex + '.uvFilterSize',fileNode + '.uvFilterSize')
                                            cmds.connectAttr(placeTex + '.coverage',fileNode + '.coverage')
                                            cmds.connectAttr(placeTex + '.translateFrame',fileNode + '.translateFrame')
                                            cmds.connectAttr(placeTex + '.rotateFrame',fileNode + '.rotateFrame')
                                            cmds.connectAttr(placeTex + '.mirrorU',fileNode + '.mirrorU')
                                            cmds.connectAttr(placeTex + '.mirrorV',fileNode + '.mirrorV')
                                            cmds.connectAttr(placeTex + '.stagger',fileNode + '.stagger')
                                            cmds.connectAttr(placeTex + '.wrapU',fileNode + '.wrapU')
                                            cmds.connectAttr(placeTex + '.wrapV',fileNode + '.wrapV')
                                            cmds.connectAttr(placeTex + '.repeatUV',fileNode + '.repeatUV')
                                            cmds.connectAttr(placeTex + '.offset',fileNode + '.offset')
                                            cmds.connectAttr(placeTex + '.rotateUV',fileNode + '.rotateUV')
                                            cmds.connectAttr(placeTex + '.noiseUV',fileNode + '.noiseUV')
                                            cmds.connectAttr(placeTex + '.vertexUvOne',fileNode + '.vertexUvOne')
                                            cmds.connectAttr(placeTex + '.vertexUvTwo',fileNode + '.vertexUvTwo')
                                            cmds.connectAttr(placeTex + '.vertexUvThree',fileNode + '.vertexUvThree')
                                            cmds.connectAttr(placeTex + '.vertexCameraOne',fileNode + '.vertexCameraOne')
                                            
                                            #set texture node path 
                                            cmds.setAttr(fileNode+'.fileTextureName',texFullName,type='string') 
                                            
                                                                                    
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance                                         
                                            if(paramtersList[i] == 'specularRoughness'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop +'.'+paramtersList[i]) 
                                            
                                            #if slot is baseColor plug it in to the shader
                                            elif(paramtersList[i] == 'baseColor'):
                                                cmds.setAttr(selLoop+'.base' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                            
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance    
                                            elif(paramtersList[i] == 'metalness'):
                                                cmds.setAttr(selLoop+'.metalness' ,1)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop + '.' +paramtersList[i] )
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string') 
                                            
                                            #if slot is emission plug it in to the shader    
                                            elif(paramtersList[i] == 'emissionColor'):
                                                cmds.setAttr(selLoop+'.emission' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                                
                                            #if slot is Normal plug it in to the shader
                                            #set color space to raw
                                            #change to Tangent Space Normals
                                            #uncheck  flip r and flip g
                                            elif(paramtersList[i] == 'normalCamera'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                bmpNode = cmds.shadingNode( 'bump2d', asUtility=True)
                                                cmds.setAttr(bmpNode + '.aiFlipR',0)
                                                cmds.setAttr(bmpNode + '.aiFlipG',0)
                                                cmds.setAttr(bmpNode + '.bumpInterp',1)
                                                cmds.connectAttr(fileNode + '.outAlpha',bmpNode + '.bumpValue') 
                                                cmds.connectAttr(bmpNode + '.outNormal',selLoop +'.'+paramtersList[i])

                                            #if slot is Height plug it in to the shaderGroup
                                            #set color space to raw
                                            #set alpha is Luminance
                                            elif(paramtersList[i] == 'Height'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                dispNode = cmds.shadingNode( 'displacementShader', asUtility=True)
                                                cmds.connectAttr(fileNode + '.outAlpha',dispNode + '.displacement') 
                                                cmds.connectAttr(dispNode + '.displacement',shadingGroup[0] +'.displacementShader')                                         
                                                
                                            #if it's anyslot except above connect it directly  
                                            else:
                                                cmds.connectAttr(fileNode + '.outColor',selLoop +'.'+paramtersList[i]) 
                        
                        else:
                            print('Cannot find '+newShaderName[0]+' in ' + file)
                            
                            
                        if (self.searchForString(shadingGroup[0], file)):                            
                           #search if the file ends with the correct extension or not
                            if(file.endswith(fileExtention)):
                                #search for the material slots paramaters
                                for i in range(0,len(paramtersList)):
                                    #if paramaters found in dic take user input
                                    if(paramtersList[i] in dictexNameUserInput):
                                        texName             = dictexNameUserInput.get(paramtersList[i])
                                        print(texName)
                                        #search for user names input in the texture it self
                                        if(-1 < file.find(texName)):
                                            texFullName = path +'/' + file
                                            print(texFullName + 'found')
                                       
                                            #Create t7exture node and make default connections
                                            fileNode      = cmds.shadingNode('file',asTexture = True, isColorManaged =True , name = 'Tex_'+ materialNode +'_'+ paramtersList[i])
                                            placeTex     = cmds.shadingNode('place2dTexture',asTexture = True)
                                            

                                            cmds.connectAttr(placeTex + '.outUV',fileNode + '.uvCoord')
                                            cmds.connectAttr(placeTex + '.uvFilterSize',fileNode + '.uvFilterSize')
                                            cmds.connectAttr(placeTex + '.coverage',fileNode + '.coverage')
                                            cmds.connectAttr(placeTex + '.translateFrame',fileNode + '.translateFrame')
                                            cmds.connectAttr(placeTex + '.rotateFrame',fileNode + '.rotateFrame')
                                            cmds.connectAttr(placeTex + '.mirrorU',fileNode + '.mirrorU')
                                            cmds.connectAttr(placeTex + '.mirrorV',fileNode + '.mirrorV')
                                            cmds.connectAttr(placeTex + '.stagger',fileNode + '.stagger')
                                            cmds.connectAttr(placeTex + '.wrapU',fileNode + '.wrapU')
                                            cmds.connectAttr(placeTex + '.wrapV',fileNode + '.wrapV')
                                            cmds.connectAttr(placeTex + '.repeatUV',fileNode + '.repeatUV')
                                            cmds.connectAttr(placeTex + '.offset',fileNode + '.offset')
                                            cmds.connectAttr(placeTex + '.rotateUV',fileNode + '.rotateUV')
                                            cmds.connectAttr(placeTex + '.noiseUV',fileNode + '.noiseUV')
                                            cmds.connectAttr(placeTex + '.vertexUvOne',fileNode + '.vertexUvOne')
                                            cmds.connectAttr(placeTex + '.vertexUvTwo',fileNode + '.vertexUvTwo')
                                            cmds.connectAttr(placeTex + '.vertexUvThree',fileNode + '.vertexUvThree')
                                            cmds.connectAttr(placeTex + '.vertexCameraOne',fileNode + '.vertexCameraOne')
                                            
                                            #set texture node path 
                                            cmds.setAttr(fileNode+'.fileTextureName',texFullName,type='string') 
                                            
                                                                                    
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance                                         
                                            if(paramtersList[i] == 'specularRoughness'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop +'.'+paramtersList[i]) 
                                            
                                            #if slot is baseColor plug it in to the shader
                                            elif(paramtersList[i] == 'baseColor'):
                                                cmds.setAttr(selLoop+'.base' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                            
                                            #if slot is roughness plug it in to the shader
                                            #set colorspace to Raw
                                            #set alpha is Luminance    
                                            elif(paramtersList[i] == 'metalness'):
                                                cmds.setAttr(selLoop+'.metalness' ,1)
                                                cmds.connectAttr(fileNode + '.outAlpha',selLoop + '.' +paramtersList[i] )
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string') 
                                            
                                            #if slot is emission plug it in to the shader    
                                            elif(paramtersList[i] == 'emissionColor'):
                                                cmds.setAttr(selLoop+'.emission' ,1)
                                                cmds.connectAttr(fileNode + '.outColor',selLoop + '.' +paramtersList[i] ) 
                                                
                                            #if slot is Normal plug it in to the shader
                                            #set color space to raw
                                            #change to Tangent Space Normals
                                            #uncheck  flip r and flip g
                                            elif(paramtersList[i] == 'normalCamera'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                bmpNode = cmds.shadingNode( 'bump2d', asUtility=True)
                                                cmds.setAttr(bmpNode + '.aiFlipR',0)
                                                cmds.setAttr(bmpNode + '.aiFlipG',0)
                                                cmds.setAttr(bmpNode + '.bumpInterp',1)
                                                cmds.connectAttr(fileNode + '.outAlpha',bmpNode + '.bumpValue') 
                                                cmds.connectAttr(bmpNode + '.outNormal',selLoop +'.'+paramtersList[i])

                                            #if slot is Height plug it in to the shaderGroup
                                            #set color space to raw
                                            #set alpha is Luminance
                                            elif(paramtersList[i] == 'Height'):
                                                cmds.setAttr(fileNode + '.colorSpace' ,'Raw',type ='string')
                                                cmds.setAttr( fileNode + '.alphaIsLuminance', True)
                                                dispNode = cmds.shadingNode( 'displacementShader', asUtility=True)
                                                cmds.connectAttr(fileNode + '.outAlpha',dispNode + '.displacement') 
                                                cmds.connectAttr(dispNode + '.displacement',shadingGroup[0] +'.displacementShader')                                         
                                                
                                            #if it's anyslot except above connect it directly  
                                            else:
                                                cmds.connectAttr(fileNode + '.outColor',selLoop +'.'+paramtersList[i])
                        else:
                            print('Cannot find '+shadingGroup[0]+' in ' + file)



plugin = SubstanceImporter()




