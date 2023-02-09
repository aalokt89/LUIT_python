#!/usr/bin/env python3
import os


def getDirDetails(path=os.getcwd()):
    myFiles = os.listdir(path)
    fileList = []

    for root, dirs, files in os.walk(path):
        for file in files:
            fileDict = {'path': os.path.join(
                root, file), 'size': os.path.getsize(os.path.join(root, file))}
            fileList.append(fileDict)

    return fileList

    # for file in myFiles:
    #     filePath = os.path.realpath(file)
    #     fileSize = os.path.getsize(file)

    #     fileInfo = {'path': filePath, 'size:': fileSize}

    #     fileList.append(fileInfo)

    # return fileList


pathFiles = getDirDetails("/Users/aaloktrivedi/LUIT/Python")

print(pathFiles)
