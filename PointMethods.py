def parsePointLine(line):
    point = []
    line = line.rstrip()
    x = line.split(",")
    for i in x:
        point.append(float(i))
    return point

def checkPoint(point, voxelBord):
    x = point[0]
    y = point[1]
    z = point[2]
    w = voxelBord[0]
    e = voxelBord[1]
    s = voxelBord[2]
    n = voxelBord[3]
    d = voxelBord[4]
    u = voxelBord[5]
    if ((x > w and x <= e) and (y > s and y <= n) and (z > d and z <= u)):
        return True
    else:
        return False
