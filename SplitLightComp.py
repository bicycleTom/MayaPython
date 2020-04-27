import nuke

def main(node):

	if node.Class() != "Read":
		nuke.message("Select an EXR Read node.")
	else:
		autocomp(node)

def shuffleAll(node, layer):
	shuffleNode = nuke.nodes.Shuffle(label='[value in]', inputs=[node])
	shuffleNode['in'].setValue(layer)

	return shuffleNode

def removeAll(node):
	removeNode = nuke.nodes.Remove(label='[value channels2]')

	return removeNode

def shuffleCopyOut(node):
	shuffleCopyNode = nuke.nodes.ShuffleCopy(label='[value out]')

	return shuffleCopyNode

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

		shuffleCopyNode = nuke.nodes.ShuffleCopy(label='[value out]')
		shuffleCopyNode['out'].setValue(str(layer))
		shuffleCopyNode.connectInput(0, removeNode)
		shuffleCopyNode.connectInput(1, removeNode)
		shuffleCopyNode['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
		shuffleCopyNode['ypos'].setValue(int(main_dot['ypos'].value() + 800))

		if (count == 1):
			mergePlus = nuke.nodes.Merge2()
			mergePlus.connectInput(1, shuffleCopyNode)
			mergePlus['operation'].setValue('plus')
			mergePlus['also_merge'].setValue('all')
			mergePlus['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
			mergePlus['ypos'].setValue(int(main_dot['ypos'].value() + 855))
			prevMerge = mergePlus
		
		if (count > 1):
			mergePlus = nuke.nodes.Merge2()
			mergePlus.connectInput(1, shuffleCopyNode)
			mergePlus['operation'].setValue('plus')
			mergePlus['also_merge'].setValue('all')
			mergePlus['xpos'].setValue(int(main_dot['xpos'].value() - x_shift))
			mergePlus['ypos'].setValue(int(main_dot['ypos'].value() + 855))
			mergePlus.connectInput(1, prevMerge)
			prevMerge = mergePlus

	copy_dot = nuke.nodes.Dot(xpos=prevMerge.xpos() - 50 , ypos=main_dot_end.ypos())
	copy_dot.connectInput(0, main_dot_end)

	copyNode = nuke.nodes.Copy(xpos=prevMerge.xpos(), ypos=copy_dot.ypos() + 75)
	copyNode.connectInput(0, copy_dot)
	copyNode.connectInput(1, prevMerge)

def addPlate(node):
	plate = nuke.nodes.Reformat()



"""
from PyQt4 import QtGui

def qt_test():
	label = QtGui.QLable("testing")
	label.show

"""