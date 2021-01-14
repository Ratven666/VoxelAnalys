def parseVoxLine(line):
    fLine = []
    line = line.rstrip()
    x = line.split(",")
    for i in x:
        fLine.append(float(i))
    return fLine


def createVoxrlsDic(VoxelCenterFilePath = "sourse/VoxelCenter.txt"):
    voxels = {}
    with open(VoxelCenterFilePath, "r") as voxCenter:
        for line in voxCenter:
            temp = parseVoxLine(line)
            voxels[int(temp[0])] = [temp[1], temp[2], temp[3]]
    return voxels

def createBorderOfVox(voxel, voxelsSize=[5,5,5]):
    border = []
    x = voxel[0]
    y = voxel[1]
    z = voxel[2]
    border.append(x - voxelsSize[0] / 2)
    border.append(x + voxelsSize[0] / 2)
    border.append(y - voxelsSize[1] / 2)
    border.append(y + voxelsSize[1] / 2)
    border.append(z - voxelsSize[2] / 2)
    border.append(z + voxelsSize[2] / 2)
    return border

def createBorderDict(voxDict):
    bord = {}
    for k, v in voxDict.items():
        bord[k] = createBorderOfVox(v)
    return bord




