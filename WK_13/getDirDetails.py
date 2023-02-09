#!/usr/bin/env python3
import os


def getDirDetails(path=os.getcwd()):
    path = input("Enter path: ")
    fileList = []
    pathExists = os.path.exists(path)

    if pathExists:
        for root, dirs, files in os.walk(path):
            for file in files:
                filePath = os.path.join(root, file)
                fileSize = os.path.getsize(os.path.join(root, file))

                fileDict = {'path': filePath, 'size': fileSize}
                fileList.append(fileDict)

        return fileList

    else:
        print(f"Error: The path {path} does not exist.")
        getDirDetails()


pathFiles = getDirDetails()

for i in pathFiles:
    print(i)
