#!/usr/bin/env python3
import os


def getDirDetails(path=os.getcwd()):
    # myFiles = os.listdir(path)
    fileList = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filePath = os.path.join(root, file)
            fileSize = os.path.getsize(os.path.join(root, file))

            fileDict = {'path': filePath, 'size': fileSize}
            fileList.append(fileDict)

    return fileList

    # for file in myFiles:
    #     filePath = os.path.realpath(file)
    #     fileSize = os.path.getsize(file)

    #     fileInfo = {'path': filePath, 'size:': fileSize}

    #     fileList.append(fileInfo)

    # return fileList


pathFiles = getDirDetails("/Users/aaloktrivedi/LUIT/Projects/LUIT_python")

print(pathFiles)
