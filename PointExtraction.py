
from SomeMetods import *

createScanFolders()

def parsePoint(line):
    point = []
    for i in line:
        point.append(float(i))
    return point

voxelsSize = [5, 5, 5]

def createVoxrls():
    voxels = []
    with open("sourse/VoxelCenter.txt", "r") as voxCenter:
        for line in voxCenter:
            line = line.rstrip()
            x = line.split(",")
            voxels.append(parsePoint(x))
    return voxels

voxels = createVoxrls()
print(voxels)

def createBorder(voxel, voxelsSize):
    border = [int(voxel[0])]
    x = voxel[1]
    y = voxel[2]
    z = voxel[3]
    border.append(x - voxelsSize / 2)
    border.append(x + voxelsSize / 2)
    border.append(y - voxelsSize / 2)
    border.append(y + voxelsSize / 2)
    border.append(z - voxelsSize / 2)
    border.append(z + voxelsSize / 2)
    return border

def checkPoint(point, voxel):
    x = point[0]
    y = point[1]
    z = point[2]
    w = voxel[1]
    e = voxel[2]
    s = voxel[3]
    n = voxel[4]
    d = voxel[5]
    u = voxel[6]
    if ((x>w and x<e) and (y>s and y<n) and (z>d and z<u)):
        return True
    else:
        return False




def createScanFolders():
    creatrFolder("Point_EXTR")
    scanList = os.listdir("sourse/Scan")
    for scan in scanList:
        scanDir = scan.split(".")[0]
        path = "Point_EXTR/" + scanDir
        creatrFolder(path)
