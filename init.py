import maya.cmds as cmds
import math as math
import random as random
import json
import numpy.random import choice

filePath = "/assets" # TODO: Filing heirarchy
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

        self.startBtn = cmds.button(label = "Start Generation", command = self.generate)

        # display
        cmds.showWindow()

    def generate(self, *args):

class FileManager:

    # load files from path, then import into maya
    def load(self):
        files = cmds.getFileList(folder = filePath, filespec = '*.%s' % fileType) # all.obj
        if len(files) == 0:
            cmds.warning("No files in the folder found.")
        else:
            for i in files:
                cmds.file(filePath + i, i = True)

class Rarity:
    def __init(self, path, json):
        with open(path + '/' + json) as json_file:
            self.rarities = json.load(json_file)

    def pick_attributes(self, category):
        choices = list(self.rarities[category].keys())
        probabilities = list(map(lambda x: x / 100.0, list(self.rarities[category].values())))
        draw = choice(choices, 1, p = probabilities)[0]
        return draw        

class Generator:
    DNA_DELIMITER = "-"

    def __init__(self, supply):
        self.supply = supply

    def createDNA(_layers):
        randNum = []
        for layer in _layers:
            totalWeight = 0

            for element in layer.elements:
                totalWeight += element.weight

            random = math.floor(random.randint(1, 999) * totalWeight)

            i = 0
            while i < len(layer.elements):
                random -= layer.elements[i].weight
                if(random < 0):
                    return randNum.push(layer.elements[i])
        return randNum.join(DNA_DELIMITER)

    def filterDNAOptions(_dna):
        dnaItems = _dns.split(DNA_DELIMITER)
        filteredDNA = filter(queryDNA, element) # Needs revision
        return filteredDNA.join(DNA_DELIMITER)

    def removeQueryStrings(_dna):
        query = /(\?.*$/)
        return _dna.replace(query, "")

    def queryDNA():
        query = /(\?.*$/)
        queryString = query.exec(element)
        if not queryString:
            return True

    def isDNAUnique(_dnaList = set(), _dna = ""):
        _filteredDNA = filterDNAOptions(_dna)
        if _filteredDNA not in _dnaList:
            return True


myWindow = Window()
