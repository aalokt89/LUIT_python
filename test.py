import os
import datetime
import json


def convertDate(timestamp):
    d = datetime.datetime.utcfromtimestamp(timestamp)
    formatedDate = d.strftime('%b %d, %Y')

    return formatedDate


def getDirDetails(path=os.getcwd()):
    fileList = []
    pathExists = os.path.exists(path)
    isFile = os.path.isfile(path)
    isDir = os.path.isdir(path)

    if pathExists and isDir:
        # do stuff
        for root, dirs, files in os.walk(path):
            for file in files:
                print(os.path.join(root, file))
                # get file path
                filePath = os.path.join(root, file)
                # get file size
                fileSize = round(os.path.getsize(filePath) / 1024, 1)
                # get and convert creation date
                fileCreationDate = convertDate(os.path.getctime(filePath))

                fileDict = {
                    'file_name': file,
                    'path': filePath,
                    'size_kb': fileSize,
                    "date_created": fileCreationDate
                }

                # add file dicts into the list
                fileList.append(fileDict)

        pathFilesJSON = json.dumps(fileList, indent=4)

        return pathFilesJSON

    elif pathExists and isFile:
        print(f"Error: The path '{path}' must be a directory.")

    elif pathExists == False:
        print(f"Error: The path '{path}' does not exist.")


print(getDirDetails("/Users/aaloktrivedi/LUIT/Projects/LUIT_python"))
