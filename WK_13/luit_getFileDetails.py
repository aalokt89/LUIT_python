import os


def getFiles():
    myPWD = os.getcwd()
    myFiles = os.listdir(myPWD)
    fileList = []

    for file in myFiles:
        filePath = os.path.abspath(file)
        fileSize = os.path.getsize(file)

        fileInfo = {'path': filePath, 'size:': fileSize}

        fileList.append(fileInfo)

    return fileList


pwdFiles = getFiles()

print(pwdFiles)
