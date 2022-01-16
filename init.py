import maya.cmds as cmds
import math as math
import random as random
import json
import numpy.random import choice

# custom library
import dna
import rarity
import attribute

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

    def generate(self, *args):

class FileManager:

    # load files from path, then import into maya
    def load(self, filePath):
        files = cmds.getFileList(folder = filePath, filespec = '*.%s' % fileType) # all.obj
        if len(files) == 0:
            cmds.warning("No files in the folder found.")
        else:
            for i in files:
                cmds.file(filePath + i, i = True)


myWindow = Window()
