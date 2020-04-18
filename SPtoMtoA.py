import maya.cmds as cmds
import pymel.core as pm
from os import listdir
import os.path

def main():
	basicFilter = "Image Files(*.exr *.png)"
	global path
	path = pm.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fm=3)
	files = listdir(path[0])
	global spfiles
	spfiles = []
	print (spfiles)
	for item in files:
		fileTypes = ('1001.exr', '1001.png')
		if (item.endswith(fileTypes)):
			spfiles.append(item)
	spfiles = [file.replace('1001', '<udim>') for file in spfiles]

	#matching = [s for s in spfiles if "1001" in s]
	#print matching

	CreateMaterial()

def CreateFileTexture(self, colorManagement = True):
	colorFile = cmds.shadingNode("aiImage", asTexture = True, isColorManaged = colorManagement)

def CreateMaterial():
	#SG

	#aiStandardSurface
	shader = cmds.shadingNode("aiStandardSurface", asShader = True, name = "substancePainter")

	#BaseColor Texture
	colorFile = cmds.shadingNode("aiImage", asTexture = True, name = "BaseColor")
	cmds.connectAttr(colorFile + ".outColor", shader + ".baseColor")
	cmds.setAttr('%s.filename' % colorFile, path[0] + '/' + ''.join(s for s in spfiles if "BaseColor" in s), type="string")
	cmds.setAttr(colorFile + ".colorSpace", "Raw", type="string" )

	#Roughness Texture
	roughnessFile = cmds.shadingNode("aiImage", asTexture = True, name = "Roughness")
	cmds.connectAttr(roughnessFile + ".outColorR", shader + ".specularRoughness")
	cmds.setAttr('%s.filename' % roughnessFile, path[0] + '/' + ''.join(s for s in spfiles if "Roughness" in s), type="string")
	cmds.setAttr(roughnessFile + ".colorSpace", "Raw", type="string")

	#Normal Texture
	normalFile = cmds.shadingNode("aiImage", asTexture = True, name = "Normal")
	normalMap = cmds.shadingNode("aiNormalMap", asUtility = True, name = "NormalMap")
	cmds.connectAttr(normalMap + ".outValue", shader + ".normalCamera")
	cmds.connectAttr(normalFile + ".outColor", normalMap + ".input")
	cmds.setAttr('%s.filename' % normalFile, path[0] + '/' + ''.join(s for s in spfiles if "Normal" in s), type="string")
	cmds.setAttr(normalFile + ".colorSpace", "Raw", type="string")

	#Opacity Texture
	opacityFile = cmds.shadingNode("aiImage", asTexture = True, name = "Opacity")
	cmds.connectAttr(opacityFile + ".outColor", shader + ".opacity")
	cmds.setAttr(opacityFile + ".ignoreMissingTextures", 1)
	cmds.setAttr(opacityFile + ".missingTextureColor", 1, 1, 1)
	cmds.setAttr('%s.filename' % opacityFile, path[0] + '/' + ''.join(s for s in spfiles if "Opacity" in s), type="string")
	cmds.setAttr(opacityFile + ".colorSpace", "Raw", type="string")

	#Metalness Texture
	metalnessFile = cmds.shadingNode("aiImage", asTexture = True, name = "Metalness")
	cmds.setAttr('%s.filename' % metalnessFile, path[0] + '/' + str(spfiles[0]), type="string")
	cmds.setAttr(metalnessFile + ".colorSpace", "Raw", type="string")

	return shader


"""
testing below

file // Result: message caching frozen isHistoricallyInteresting nodeState binMembership uvCoord uCoord vCoord uvFilterSize uvFilterSizeX uvFilterSizeY filter filterOffset invert alphaIsLuminance colorGain 
colorGainR colorGainG colorGainB colorOffset colorOffsetR colorOffsetG colorOffsetB alphaGain alphaOffset defaultColor defaultColorR defaultColorG defaultColorB outColor outColorR outColorG outColorB 
outAlpha fileTextureName fileTextureNamePattern computedFileTextureNamePattern disableFileLoad useFrameExtension frameExtension frameOffset useHardwareTextureCycling startCycleExtension endCycleExtension 
byCycleIncrement forceSwatchGen filterType filterWidth preFilter preFilterRadius useCache useMaximumRes uvTilingMode explicitUvTiles explicitUvTiles.explicitUvTileName explicitUvTiles.explicitUvTilePosition 
explicitUvTiles.explicitUvTilePositionU explicitUvTiles.explicitUvTilePositionV baseExplicitUvTilePosition baseExplicitUvTilePositionU baseExplicitUvTilePositionV uvTileProxyDirty uvTileProxyGenerate 
uvTileProxyQuality coverage coverageU coverageV translateFrame translateFrameU translateFrameV rotateFrame doTransform mirrorU mirrorV stagger wrapU wrapV repeatUV repeatU repeatV offset offsetU offsetV 
rotateUV noiseUV noiseU noiseV blurPixelation vertexCameraOne vertexCameraOneX vertexCameraOneY vertexCameraOneZ vertexCameraTwo vertexCameraTwoX vertexCameraTwoY vertexCameraTwoZ vertexCameraThree 
vertexCameraThreeX vertexCameraThreeY vertexCameraThreeZ vertexUvOne vertexUvOneU vertexUvOneV vertexUvTwo vertexUvTwoU vertexUvTwoV vertexUvThree vertexUvThreeU vertexUvThreeV objectType rayDepth 
primitiveId pixelCenter pixelCenterX pixelCenterY exposure hdrMapping hdrExposure dirtyPixelRegion ptexFilterType ptexFilterWidth ptexFilterBlur ptexFilterSharpness ptexFilterInterpolateLevels 
colorProfile colorSpace ignoreColorSpaceFileRules workingSpace colorManagementEnabled colorManagementConfigFileEnabled colorManagementConfigFilePath outSize outSizeX outSizeY fileHasAlpha outTransparency
outTransparencyR outTransparencyG outTransparencyB infoBits aiUserOptions aiFilter aiAutoTx aiMipBias aiUseDefaultColor // 

aiimage // Result: message caching frozen isHistoricallyInteresting nodeState binMembership outColor outColorR outColorG outColorB outAlpha outTransparency outTransparencyR outTransparencyG outTransparencyB 
filename colorSpace filter mipmapBias singleChannel startChannel swrap twrap sscale tscale sflip tflip soffset toffset swapSt uvcoords uvcoordsX uvcoordsY uvset multiply multiplyR multiplyG multiplyB 
offset offsetR offsetG offsetB ignoreMissingTextures missingTextureColorA missingTextureColor missingTextureColorR missingTextureColorG missingTextureColorB aiUserOptions autoTx colorManagementConfigFileEnabled 
colorManagementConfigFilePath colorManagementEnabled colorProfile colorSpace workingSpace useFrameExtension frame ignoreColorSpaceFileRules // 



import maya.cmds as cmds
import pymel.core as pm  
from os import listdir   
  
def main(*arg):
    selectionList = pm.ls(sl=True)

    basicFilter = "Image Files (*.TGA *.tga *.DDS *.dds *.PNG *.png *.exr)"
    global path
    path = pm.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fm=3)
    files = listdir(path[0])
    global ddsFiles
    ddsFiles = []
    print (ddsFiles)
    for item in files:
        fileEndings = ('.TGA', '.tga', '.DDS', '.dds', '.PNG', '.png', '.exr')
        if (item.endswith(fileEndings)):
            ddsFiles.append(item)
    mat()    

def applyMaterial(node):
    if cmds.objExists(node):
                
        # base
        shd = cmds.shadingNode('aiStandardSurface', name = "%s_aiStandardSurface " % node, asShader=True)
        shdSG = cmds.sets(name='%sSG' % shd, empty=True, renderable=True, noSurfaceShader=True)
        cmds.connectAttr('%s.outColor' % shd, '%s.surfaceShader' % shdSG)
        cmds.sets(node, e=True, forceElement=shdSG)
        # basecolor
        fileBaseColor = cmds.shadingNode('file', name="%s_fileBasseColor" % node, asTexture=True )
        cmds.setAttr(fileBaseColor + '.colorSpace', 'sRGB', type='string')
        cmds.connectAttr('%s.outColor' % fileBaseColor, '%s.baseColor' % shd)  
        cmds.setAttr('%s.fileTextureName' % fileBaseColor, path[0] + '/' + str(ddsFiles[0]), type="string")
        # roughness
        fileRoughness = cmds.shadingNode('file', name="%s_fileRoughness" % node, asTexture=True )
        cmds.setAttr(fileRoughness + '.colorSpace', 'Raw', type='string')
        #cmds.setAttr(fileRoughness + '.colorSpace', 'Raw', type='bool')
        cmds.connectAttr('%s.outColorR' % fileRoughness, '%s.specularRoughness' % shd)
        cmds.setAttr('%s.fileTextureName' % fileRoughness, path[0] + '/' + str(ddsFiles[4]), type="string")
        # metalic
        fileMetalic = cmds.shadingNode('file', name="%s_fileMetalic" % node, asTexture=True )
        cmds.setAttr(fileMetalic + '.colorSpace', 'Raw', type='string')
        cmds.connectAttr('%s.outColorR' % fileMetalic, '%s.metalness' % shd)
        cmds.setAttr('%s.fileTextureName' % fileMetalic, path[0] + '/' + str(ddsFiles[2]), type="string")    
        #normal   
        fileNormal = cmds.shadingNode('file', name="%s_fileNormal" % node, asUtility=True)
        bump = cmds.shadingNode('bump2d', name="%s_bump2d" % node, asTexture=True)
        cmds.setAttr(fileNormal + '.colorSpace', 'Raw', type='string')
        cmds.setAttr(bump + ".bumpInterp", 1)
        cmds.connectAttr('%s.outAlpha' % fileNormal, '%s.bumpValue' % bump)
        cmds.connectAttr(bump + ".outNormal", shd + ".normalCamera")
        cmds.setAttr('%s.fileTextureName' % fileNormal, path[0] + '/' + str(ddsFiles[3]), type="string")
        #ambient
        fileAmbient = cmds.shadingNode('file', name="%s_fileAmbient" % node, asTexture=True)
        cmds.setAttr(fileAmbient + '.colorSpace', 'sRGB', type='string')
        #cmds.connectAttr(fileAmbient + ".outAlpha", shd + ".base")        

def mat(*arg):
    selection = cmds.ls(sl=True)
    myObjectName = selection[0]
    
    for myObjectNames in selection:  
        applyMaterial(myObjectName)   
        
#pm.window(title='Auto ShaderLab', width=200)
#pm.columnLayout(adjustableColumn=True)

#pm.button(label = 'applyMaterial', command=main)
#pm.showWindow()

#######################################
#more#
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
"""