import os
from PointMethods import *

def createScanList(scanPath="sourse/Scan"):
    return os.listdir(scanPath)

def readScan(scanName, scanPath="sourse/Scan/"):
    scan = []
    path = scanPath + scanName
    with open(path, "r") as s:
        for line in s:
            scan.append(parsePointLine(line))
    return scan



# scan = readScan("sc280720.txt")
#
# for i in scan:
#     print(i)

# scanList = createScanList()
# print(scanList)