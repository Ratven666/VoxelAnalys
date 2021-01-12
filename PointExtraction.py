from CreateStruct import *
from VoxelMetods import *
from ScanMetods import *

def structSan(scanName, bord):
    scan = readScan(scanName)
    for p in scan:
        for k,v in bord.items():
            if (checkPoint(p, v)):
                filePath = "Point_EXTR/" + scanName.split(".")[0] + "/" + str(k) + ".txt"
                file = open(filePath, "a")
                s = ""
                for i in p:
                    s += str(i)
                    s += ","
                s = s[:-1] + "\n"
                file.write(s)
                file.close()


