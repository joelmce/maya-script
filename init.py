import maya.cmds as cmds
import math as math
import random as random
import json

# custom library
import filemanager

# filePath = "/assets"
fileType = "obj"

class Window(object):

    # constructor
    def __init__(self):
        self.window = "Akuma Generator"
        self.title = "Generation Settings"
        self.size = (400, 400)


        # close window if window is open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window = True)

        # create new window instance
        self.window = cmds.window(self.window, title = self.title, widthHeight = self.size)

        cmds.columnLayout(adjustableColumn = True)

        cmds.text(self.title)
        cmds.seperator(height = 20)

        self.collectionName = cmds.textFieldGrp(label = "Collection name:")
        self.description = cmds.textFieldGrp(label = "Description:")
        self.supply = cmds.intSlideGrp(field = True, label = "Supply:", minValue = 1, maxValue = 10000, value = 1)
        self.filePath = cmds.textFieldGrp(label = "File Path:")

        self.startBtn = cmds.button(label = "Start Generation", command = self.generate)

        # display
        cmds.showWindow()
