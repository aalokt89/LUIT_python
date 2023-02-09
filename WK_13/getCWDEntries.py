#!/usr/bin/env python3
import os


def getCWDEntries():
    myCWD = os.getcwd()
    entryList = []

    with os.scandir(myCWD) as entries:
        for entry in entries:
            entryPath = os.path.abspath(entry)
            entrySize = os.path.getsize(entry)

            entryInfo = {'path': entryPath, 'size:': entrySize}

            entryList.append(entryInfo)

    return entryList


cwdEntries = getCWDEntries()

print(cwdEntries)
