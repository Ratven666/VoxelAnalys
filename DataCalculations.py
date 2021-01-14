from CreateStruct import *
from PlaneAprox import *
from PointExtraction import *
import os

from VoxelMetods import *


def allSourseScanStruct(bord, dirPath = "sourse/Scan/"):
    createScanFolders()
    for cur_dir, dirs, files in os.walk(dirPath):
        for file in files:
            structSan(file,bord)


def getResult(dataFold = "Point_EXTR"):
    for cur_dir, dirs, files in os.walk(dataFold):
        if (len(files) > 0):
            fileName = cur_dir.split("\\")[1] + ".txt"
            filePath = dataFold + "/" + fileName
            fw = open(filePath, "a")
            fw.write("Number\tA\tB\tC\tmX\tmY\tmZ\tMSE\n")
            for file in files:
                number = file.split(".")[0]
                abc = fitPlane(file, dataFold + "/" + cur_dir.split("\\")[1] + "/")
                mse = calcMSEofPlaneArp(file, dataFold + "/" + cur_dir.split("\\")[1] + "/")
                meanXYZ = calcMeanCoord(file, dataFold + "/" + cur_dir.split("\\")[1] + "/")
                fw.write(number + "\t" + str(abc[0]) + "\t" + str(abc[1]) + "\t" + str(abc[2]) + "\t" + str(meanXYZ[0]) + "\t"
                         + str(meanXYZ[1]) + "\t" + str(meanXYZ[2]) + "\t" + str(mse) + "\n")
            fw.close()


vox = createVoxrlsDic()
bord = createBorderDict(vox)

allSourseScanStruct(bord)
getResult()
