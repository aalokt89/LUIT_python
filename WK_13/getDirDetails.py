#!/usr/bin/env python3
import os


def getDirDetails(path=os.getcwd()):
    myFiles = os.listdir(path)
    fileList = []

    for file in myFiles:
        filePath = os.path.realpath(file)
        fileSize = os.path.getsize(file)

        fileInfo = {'path': filePath, 'size:': fileSize}

        fileList.append(fileInfo)

    return fileList


pathFiles = getDirDetails()

print(pathFiles)
