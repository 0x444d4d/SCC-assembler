# This Python file uses the following encoding: utf-8
import sys
import tempfile

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from qtSCC import Ui_qtSCC
import os
sys.path.append(os.path.abspath('../../SCC'))
import SCCUtils

class qtSCC(QMainWindow, Ui_qtSCC):
    def __init__(self, *args, **kwargs):
        super(qtSCC, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.virtual_file = tempfile.SpooledTemporaryFile(mode = "w+", encoding = "utf-8", dir = "/tmp/")
        self.binaryCode = []
        self.translationQueue = []

        self.SearchButton.clicked.connect(self.onSearchButtonClicked)
        self.assembleButton.clicked.connect(self.onAssembleButtonClicked)
        self.saveButton.clicked.connect(self.onSaveButtonClicked)
        self.fileList.itemClicked.connect(self.onFileListItemClicked)
        self.translateList.itemClicked.connect(self.onTranslateListItemClicked)

        self.show()

    def onSaveButtonClicked(self):
        pass
        # fileName = self.saveEdit.text()
        # SCCUtils.writeList2File(fileName, self.binaryCode)

    def onAssembleButtonClicked(self):
        for fileName in self.translationQueue:
            binaryCode = self.assembleFile(fileName)
            binFileName = fileName.split('.')[0];
            binFileName = binFileName + ".bin"
            SCCUtils.writeList2File(binFileName, binaryCode) 
        self.translationQueue = []; 

    def onSearchButtonClicked(self):
        self.fileList.clear()
        path = self.inputEdit.text()
        path = QDir(path)
        print(path.dirName())
        path.setFilter(QDir.Files)
        contentsList = path.entryList()
        for content in contentsList:
            basePath = self.inputEdit.text()
            filePath = os.path.join(basePath, content)
            self.fileList.addItem(content)

    def onFileListItemClicked(self, item):
        basePath = self.inputEdit.text()
        filePath = os.path.join(basePath, item.text())
        self.translateList.addItem(item.text())
        self.translationQueue.append(filePath)

    def onTranslateListItemClicked(self, item):
        self.translationQueue.remove(item.text())
        self.translateList.takeItem(self.translateList.currentRow())

    def assembleFile(self, fileName):
        with open(fileName, 'r') as inputFile:
            SCCUtils.strip_input(self.virtual_file, inputFile)
            SCCUtils.operateFile(self.virtual_file, SCCUtils.resolveDirections)
            binaryCode = SCCUtils.operateFile(self.virtual_file, SCCUtils.translate)
            return binaryCode

if  __name__  ==  "__main__":
    app = QApplication([])
    window = qtSCC()
    app.exec_()
