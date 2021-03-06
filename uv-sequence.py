# Author: Nikita Kozlov
# Link: github.com/nyarstot

import maya.cmds as cmds

selection = cmds.ls(sl=True)

if len(selection) > 1:
    for i in range(1, len(selection)):
        cmds.transferAttributes(selection[0], selection[i], uvs = 2, sampleSpace = 4)
else:
    cmds.error("The number of selected objects must be greater than one")
