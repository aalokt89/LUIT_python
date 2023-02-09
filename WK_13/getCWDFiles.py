#!/usr/bin/env python3

import os


def getCWDFiles():
    myPWD = os.getcwd()
    myFiles = os.listdir(myPWD)
    fileList = []

    for file in myFiles:
        filePath = os.path.abspath(file)
        fileSize = os.path.getsize(file)

        fileInfo = {'path': filePath, 'size:': fileSize}

        fileList.append(fileInfo)

    return fileList


cwdFiles = getCWDFiles()

print(cwdFiles)
