import nuke

count = 0

mirror = -1
x_shift = 34
y_label_shift = 6
y_dot_shift = 7

#nuke.Layer('rgba', ['red', 'green', 'blue', 'alpha'])

def main(node):

	if node.Class() != "Read":
		nuke.message("Select an EXR Read node.")
	else:
		autocomp(node)
		addPlate(node)
		diagnostic(node)

#split passes from render
def autocomp(node):

	count = 0

	mirror = -1
	
	x_shift = 34

	#prev_node = node
	main_dot = nuke.nodes.Dot(xpos=node.xpos() + x_shift, ypos=node.ypos() - (120*mirror))
	main_dot.connectInput(0, node)

	main_dot_end = nuke.nodes.Dot(xpos=main_dot.xpos(), ypos=main_dot.ypos() + 950)
	main_dot_end.connectInput(0, main_dot)

	#get all aov layers
	channels = node.channels()
	layers = list(set([c.split('.')[0] for c in channels]))
	layers.sort()

	#create list of light aovs
	lights = []
	for layer in layers:
		if layer.startswith("RGBA_"):
			lights.append(layer)

	#build split lights
	for layer in lights:

		count = count + 1
		#print count

		global prevMerge
		global copy_dot
		global copyNode

		current_dot = main_dot

		light_dots = nuke.nodes.Dot()
		light_dots.connectInput(0, current_dot)
		light_dots['xpos'].setValue(int(current_dot['xpos'].value() + 340))
		light_dots['ypos'].setValue(int(current_dot['ypos'].value()))

		main_dot = light_dots

		shuffleNode = nuke.nodes.Shuffle(label='[value in]', inputs=[main_dot])
		shuffleNode['in'].setValue(layer)
		shuffleNode['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
		shuffleNode['ypos'].setValue(int(main_dot['ypos'].value() + 85))

		removeNode = nuke.nodes.Remove(label='[value channels2]')
		removeNode['operation'].setValue('keep')
		removeNode['channels'].setValue('rgba')
		removeNode['channels2'].setValue(str(layer))
		removeNode.connectInput(0, shuffleNode)
		removeNode['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
		removeNode['ypos'].setValue(int(main_dot['ypos'].value() + 135))

		shuffleOutNode = nuke.nodes.Shuffle(label='[value out]')
		shuffleOutNode['out'].setValue(str(layer))
		shuffleOutNode.connectInput(0, removeNode)
		shuffleOutNode['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
		shuffleOutNode['ypos'].setValue(int(main_dot['ypos'].value() + 800))

		#the first merge recieves only one input from shuffled light pass
		if (count == 1):
			mergePlus = nuke.nodes.Merge2()
			mergePlus.connectInput(1, shuffleOutNode)
			mergePlus['operation'].setValue('plus')
			mergePlus['also_merge'].setValue('all')
			mergePlus['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
			mergePlus['ypos'].setValue(int(main_dot['ypos'].value() + 855))
			prevMerge = mergePlus

		#additional merges recieve both previous merge and shuffled light pass
		if (count > 1):
			mergePlus = nuke.nodes.Merge2()
			mergePlus.connectInput(1, shuffleOutNode)
			mergePlus['operation'].setValue('plus')
			mergePlus['also_merge'].setValue('all')
			mergePlus['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
			mergePlus['ypos'].setValue(int(main_dot['ypos'].value() + 855))
			mergePlus.connectInput(0, prevMerge)
			prevMerge = mergePlus

	copy_dot = nuke.nodes.Dot(xpos=prevMerge.xpos() - 50 , ypos=main_dot_end.ypos())
	copy_dot.connectInput(0, main_dot_end)

	copyNode = nuke.nodes.Copy(xpos=prevMerge.xpos(), ypos=copy_dot.ypos() + 75)
	copyNode['from0'].setValue('rgba.alpha')
	copyNode['to0'].setValue('rgba.alpha')
	copyNode.connectInput(0, prevMerge)
	copyNode.connectInput(1, copy_dot)

#merge lights over background plate and add main comp write node
def addPlate(node):

	global mergePlateNode
	global writeNode
	
	mergePlateNode = nuke.nodes.Merge2(label='background', xpos=copyNode.xpos(), ypos=copyNode.ypos() + 175)
	mergePlateNode.connectInput(1, copyNode)

	plateRefNode = nuke.nodes.Reformat(format='2K_DCP', xpos=mergePlateNode.xpos() - 1800, ypos=mergePlateNode.ypos())
	mergePlateNode.connectInput(0, plateRefNode)

	refOutNode = nuke.nodes.Reformat(format='2K_DCP', inputs=[mergePlateNode], xpos=mergePlateNode.xpos(), ypos=mergePlateNode.ypos() + 175)

	writeNode = nuke.nodes.Write(inputs=[refOutNode], label='comp', xpos=mergePlateNode.xpos(), ypos=mergePlateNode.ypos() + 275)

#create diagnostice comp using render meta data, grades, etc.
def diagnostic(node):

	shuffleNewRgba = nuke.nodes.Shuffle(inputs=[prevMerge], label='[value out]', xpos=prevMerge.xpos() + 400, ypos=prevMerge.ypos() - y_label_shift)
	#nuke.Layer('rgba_new', ['red', 'green', 'blue', 'alpha'])
	#shuffleNewRgba['out'].setValue('rgba_new')

	removeKeepRgba = nuke.nodes.Remove(inputs=[copy_dot], xpos=copy_dot.xpos() + 300, ypos=copy_dot.ypos() - y_label_shift)
	removeKeepRgba['operation'].setValue('keep')
	removeKeepRgba['channels'].setValue('rgb')

	shuffleOldRgba = nuke.nodes.Shuffle(inputs=[removeKeepRgba], label='[value out]', xpos=removeKeepRgba.xpos(), ypos=removeKeepRgba.ypos() + 35)
	#nuke.Layer('rgba_original', ['red', 'green', 'blue', 'alpha'])
	#shuffleOldRgba['out'].setValue('rgba_original')

	mergeToDiagnostic = nuke.nodes.Merge2(inputs=[shuffleOldRgba, shuffleNewRgba], xpos=shuffleNewRgba.xpos(), ypos=shuffleOldRgba.ypos() + y_label_shift)
	mergeToDiagnostic['operation'].setValue('difference')
	mergeToDiagnostic['also_merge'].setValue('all')

	mergeDiffDot = nuke.nodes.Dot(inputs=[mergeToDiagnostic], xpos=mergeToDiagnostic.xpos() + 1800, ypos=mergeToDiagnostic.ypos() - 250)

	contactSheetDot = nuke.nodes.Dot(inputs=[mergeDiffDot], xpos=mergeDiffDot.xpos() + 250, ypos=mergeDiffDot.ypos())

	#diff the original render with the graded lights
	mergeDifference = nuke.nodes.NoOp(inputs=[mergeDiffDot], xpos=mergeDiffDot.xpos() - x_shift, ypos=mergeDiffDot.ypos() + 100)
	#mergeDifference = nuke.nodes.Merge2(inputs=[mergeDiffDot, mergeDiffDot], label='A: [value Achannels] B: [value Bchannels]', xpos=mergeDiffDot.xpos() - x_shift, ypos=mergeDiffDot.ypos() + 100)
	#mergeDifference['operation'].setValue('difference')
	#mergeDifference['Achannels'].setValue('rgba_new')
	#mergeDifference['Bchannels'].setValue('rgba_original')

	diffText = nuke.nodes.Text2(inputs=[mergeDifference], xpos=mergeDifference.xpos(), ypos=mergeDifference.ypos() + 35)
	diffText['message'].setValue('Difference')
	diffText['box'].setValue((0.0, 0.0, 2048.0, 1080.0))
	diffText['yjustify'].setValue('bottom')

	diffRef = nuke.nodes.Reformat(inputs=[diffText], xpos=mergeDifference.xpos(), ypos=mergeDifference.ypos() + 70)
	diffRef['type'].setValue('scale')
	diffRef['scale'].setValue(0.5)

	diffCrop = nuke.nodes.Crop(inputs=[diffRef], xpos=mergeDifference.xpos(), ypos=mergeDifference.ypos() + 105)
	diffCrop['box'].setValue((0.0, 0.0, 1024.0, 540.0))

	diffTrans = nuke.nodes.Transform(inputs=[diffCrop], xpos=mergeDifference.xpos(), ypos=mergeDifference.ypos() + 140)

	#layout each light as a collage
	contactRemove = nuke.nodes.Remove(inputs=[contactSheetDot], label='[value channels], [value channels2], [value channels3]', xpos=contactSheetDot.xpos() - x_shift, ypos=contactSheetDot.ypos() + 100)
	contactRemove['channels'].setValue('rgba')
	contactRemove['channels2'].setValue('rgba_new')
	contactRemove['channels3'].setValue('rgba_original')

	contactLights = nuke.nodes.LayerContactSheet(showLayerNames=True, inputs=[contactRemove], xpos=contactRemove.xpos(), ypos=contactRemove.ypos() + 35)
	contactLights['width'].setValue((1024.0))
	contactLights['height'].setValue((1080.0))

	contactCrop = nuke.nodes.Crop(inputs=[contactLights], xpos=contactRemove.xpos(), ypos=contactRemove.ypos() + 70)
	contactCrop['box'].setValue((0.0, 0.0, 1024.0, 1080.0))

	contactTrans = nuke.nodes.Transform(inputs=[contactCrop], xpos=contactRemove.xpos(), ypos=contactRemove.ypos() + 105)
	contactTrans['translate'].setValue((1024.0, 0.0))

	#merge it altogether
	mergeRef = nuke.nodes.Reformat(format='2K_DCP', xpos=mergeDifference.xpos() + 100, ypos=mergeDifference.ypos() + 280)

	#add comp result
	mergeConDiff = nuke.nodes.Merge2(inputs=[mergeRef, diffTrans], xpos=mergeDifference.xpos(), ypos=mergeDifference.ypos() + 280 + y_label_shift)
	mergeConDiff.connectInput(4, contactTrans)

	shuffleComp = nuke.nodes.Shuffle(inputs=[mergePlateNode], xpos=mergePlateNode.xpos() + 1700, ypos=mergePlateNode.ypos())
	shuffleComp['alpha'].setValue('white')

	refComp = nuke.nodes.Reformat(inputs=[shuffleComp], xpos=shuffleComp.xpos(), ypos=shuffleComp.ypos() + 35)
	refComp['type'].setValue('scale')
	refComp['scale'].setValue(0.5)

	cropComp = nuke.nodes.Crop(inputs=[refComp], xpos=shuffleComp.xpos(), ypos=shuffleComp.ypos() + 70)
	cropComp['box'].setValue((0.0, 0.0, 1024.0, 540.0))

	transComp = nuke.nodes.Transform(inputs=[cropComp], xpos=shuffleComp.xpos(), ypos=shuffleComp.ypos() + 105)
	transComp['translate'].setValue((0.0, 540.0))

	mergeComp = nuke.nodes.Merge2(inputs=[mergeConDiff, transComp], xpos=mergeConDiff.xpos(), ypos=transComp.ypos())

	reformatAll = nuke.nodes.Reformat(inputs=[mergeComp], format='2K_DCP', xpos=mergeConDiff.xpos(), ypos=mergeConDiff.ypos() + 270)

	writeSplit = nuke.nodes.Write(inputs=[reformatAll], label='split lights', xpos=mergeConDiff.xpos(), ypos=writeNode.ypos())




"""
from PyQt4 import QtGui

def qt_test():
	label = QtGui.QLable("testing")
	label.show

"""