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

	CreateMaterial()


def CreateMaterial():
	#SG

	#aiStandardSurface
	shader = cmds.shadingNode('aiStandardSurface', asShader = True, name = 'substancePainter')

	#BaseColor Texture
	colorFile = cmds.shadingNode('aiImage', asTexture = True, name = 'BaseColor')
	cmds.connectAttr(colorFile + '.outColor', shader + '.baseColor')
	cmds.setAttr('%s.filename' % colorFile, path[0] + '/' + ''.join(s for s in spfiles if 'BaseColor' in s), type='string')
	cmds.setAttr(colorFile + '.colorSpace', 'Raw', type='string' )

	#Roughness Texture
	roughnessFile = cmds.shadingNode('aiImage', asTexture = True, name = 'Roughness')
	cmds.connectAttr(roughnessFile + '.outColorR', shader + '.specularRoughness')
	cmds.setAttr('%s.filename' % roughnessFile, path[0] + '/' + ''.join(s for s in spfiles if 'Roughness' in s), type='string')
	cmds.setAttr(roughnessFile + '.colorSpace', 'Raw', type='string')

	#Normal Texture
	normalFile = cmds.shadingNode('aiImage', asTexture = True, name = 'Normal')
	normalMap = cmds.shadingNode('aiNormalMap', asUtility = True, name = 'NormalMap')
	cmds.connectAttr(normalMap + '.outValue', shader + '.normalCamera')
	cmds.connectAttr(normalFile + '.outColor', normalMap + '.input')
	cmds.setAttr('%s.filename' % normalFile, path[0] + '/' + ''.join(s for s in spfiles if 'Normal' in s), type='string')
	cmds.setAttr(normalFile + '.colorSpace', 'Raw', type='string')

	#Opacity Texture
	opacityFile = cmds.shadingNode('aiImage', asTexture = True, name = 'Opacity')
	cmds.connectAttr(opacityFile + '.outColor', shader + '.opacity')
	cmds.setAttr(opacityFile + '.ignoreMissingTextures', 1)
	cmds.setAttr(opacityFile + '.missingTextureColor', 1, 1, 1)
	cmds.setAttr('%s.filename' % opacityFile, path[0] + '/' + ''.join(s for s in spfiles if 'Opacity' in s), type='string')
	cmds.setAttr(opacityFile + '.colorSpace', 'Raw', type='string')

	#Metalness Texture
	metalnessFile = cmds.shadingNode('aiImage', asTexture = True, name = 'Metalness')
	cmds.setAttr('%s.filename' % metalnessFile, path[0] + '/' + str(spfiles[0]), type='string')
	cmds.setAttr(metalnessFile + '.colorSpace', 'Raw', type='string')

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

"""