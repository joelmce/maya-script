import json
import sys


class FileManager:

    @staticmethod
    def file_import():
        _file = open('_metadata.json')
        metadata = json.load(_file)
        cycle = 0
        while cycle <= 2222:
            for i in metadata[cycle]['attributes']:
                print(i)
                cycle = cycle + 1
        _file.close()   

    def __init__(self):
        self.file_import()

    # load files from path, then import into maya
    #def load(self, filePath):
        #files = cmds.getFileList(folder = filePath, filespec = '*.%s' % fileType) # all.obj
        #if len(files) == 0:
            #cmds.warning("No files in the folder found.")
        #else:
            #for i in files:
                #cmds.file(filePath + i, i = True)
            
start = FileManager() 
