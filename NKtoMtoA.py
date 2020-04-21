#########################################
#work in progress, to do: 
#light groups need to be paired to grades, cut_paste must contain light group name
#rendered exrs from maya must contain light grade values for some kind of passthrough expression
#########################################

import maya.cmds as cmds
from PySide2.QtGui import QClipboard

def main():

    print use_clipboard()

#def ccMtoA():


def use_clipboard():
    clipboard_text = QClipboard().text()

    return clipboard_text



"""
example pasted nuke grade node

set cut_paste_input [stack 0]
version 11.1 v1
push $cut_paste_input
Grade {
 white {1 0.5 0.25 1}
 multiply 0.5
 name Grade1
 selected true
 xpos -50
 ypos -136
}
"""