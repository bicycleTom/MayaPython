import nuke

count = 0

mirror = -1
	
x_shift = 34
y_label_shift = 6
y_dot_shift = 7

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

		#shuffleCopyNode = nuke.nodes.ShuffleCopy(label='[value out]')
		#shuffleCopyNode['out'].setValue(str(layer))
		#shuffleCopyNode.connectInput(0, removeNode)
		#shuffleCopyNode.connectInput(1, removeNode)
		#shuffleCopyNode['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
		#shuffleCopyNode['ypos'].setValue(int(main_dot['ypos'].value() + 800))

		shuffleOutNode = nuke.nodes.Shuffle(label='[value out]')
		shuffleOutNode['out'].setValue(str(layer))
		shuffleOutNode.connectInput(0, removeNode)
		shuffleOutNode['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
		shuffleOutNode['ypos'].setValue(int(main_dot['ypos'].value() + 800))

		if (count == 1):
			mergePlus = nuke.nodes.Merge2()
			mergePlus.connectInput(1, shuffleOutNode)
			mergePlus['operation'].setValue('plus')
			mergePlus['also_merge'].setValue('all')
			mergePlus['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
			mergePlus['ypos'].setValue(int(main_dot['ypos'].value() + 855))
			prevMerge = mergePlus
		
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

#merge lights over background plate
def addPlate(node):
	
	mergePlateNode = nuke.nodes.Merge2(label='background', xpos=copyNode.xpos(), ypos=copyNode.ypos() + 175)
	mergePlateNode.connectInput(1, copyNode)

	plateRefNode = nuke.nodes.Reformat(xpos=mergePlateNode.xpos() - 1800, ypos=mergePlateNode.ypos())
	plateRefNode['format'].setValue('2K_DCP')
	mergePlateNode.connectInput(0, plateRefNode)

	refOutNode = nuke.nodes.Reformat(xpos=mergePlateNode.xpos(), ypos=mergePlateNode.ypos() + 175)
	refOutNode['format'].setValue('2K_DCP')
	refOutNode.connectInput(0, mergePlateNode)

	writeNode = nuke.nodes.Write(xpos=mergePlateNode.xpos(), ypos=mergePlateNode.ypos() + 275)
	writeNode.connectInput(0, refOutNode)

def diagnostic(node):

	shuffleNewRgba = nuke.nodes.Shuffle(inputs=[prevMerge], label='[value out]', xpos=prevMerge.xpos() + 400, ypos=prevMerge.ypos() - y_label_shift)
	shuffleNewRgba['out'].setValue('rgba_new')

	removeKeepRgba = nuke.nodes.Remove(inputs=[copy_dot], xpos=copy_dot.xpos() + 300, ypos=copy_dot.ypos() - y_label_shift)
	removeKeepRgba['operation'].setValue('keep')

	shuffleOldRgba = nuke.nodes.Shuffle(inputs=[removeKeepRgba], label='[value out]', xpos=removeKeepRgba.xpos(), ypos=removeKeepRgba.ypos() + 35)
	shuffleOldRgba['out'].setValue('rgba_original')

	mergeToDiagnostic = nuke.nodes.Merge2(inputs=[shuffleNewRgba, shuffleOldRgba], xpos=shuffleNewRgba.xpos(), ypos=shuffleOldRgba.ypos() + y_label_shift)
	mergeToDiagnostic['also_merge'].setValue('all')

	mergeDiffDot = nuke.nodes.Dot(inputs=[mergeToDiagnostic], xpos=mergeToDiagnostic.xpos() + 1800, ypos=mergeToDiagnostic.ypos() - 250)

	contactSheetDot = nuke.nodes.Dot(inputs=[mergeDiffDot], xpos=mergeDiffDot.xpos() + 250, ypos=mergeDiffDot.ypos())

	mergedifference = nuke.nodes.Merge2(inputs=[mergeDiffDot, mergeDiffDot], label='A: [value Achannels] B: [value Bchannels]', xpos=mergeDiffDot.xpos() - x_shift, ypos=mergeDiffDot.ypos() + 100)






"""
from PyQt4 import QtGui

def qt_test():
	label = QtGui.QLable("testing")
	label.show

"""