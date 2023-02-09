#!/usr/bin/env python3
import os


def getDirDetails(path=os.getcwd()):
    path = input("Enter path")
    fileList = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filePath = os.path.join(root, file)
            fileSize = os.path.getsize(os.path.join(root, file))

            fileDict = {'path': filePath, 'size': fileSize}
            fileList.append(fileDict)

    return fileList


pathFiles = getDirDetails()

for i in pathFiles:
    print(i)
