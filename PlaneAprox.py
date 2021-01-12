import numpy as np
from ScanMetods import readScan

def readNumPyScan(fileName, path):
    return np.array(readScan(fileName, path))


def fitPlane(fileName, path):
    """ Метод выдает numPy матрицу коэфициентов A,B,C плоскости для уравнеия плоскости вида Ax + By + C = z"""
    xyz = readNumPyScan(fileName, path)
    a1, b1, c1, d1, b2, c2, c3, d1, d2, d3 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for line in xyz:
        a1 += line[0] ** 2
        b1 += line[0] * line[1]
        c1 += line[0]
        b2 += line[1] ** 2
        c2 += line[1]
        c3 += 1
        d1 += line[0] * line[2]
        d2 += line[1] * line[2]
        d3 += line[2]
    mA = np.array([[a1, b1, c1], [b1, b2, c2], [c1, c2, c3]])
    mD = np.array([d1, d2, d3])
    return np.linalg.solve(mA, mD)


def calcMSEofPlaneArp(fileName, path):
    """Метод возвращает СКП точек от вписываемой плоскости"""
    xyz = readNumPyScan(fileName, path)
    abc = fitPlane(fileName, path)
    sumVV = 0
    n = 0
    for line in xyz:
        v = line[2] - (abc[0] * line[0] + abc[1] * line[1] + abc[2])
        sumVV += v ** 2
        n += 1
    return (sumVV / (n - 1)) ** 0.5

def calcMeanCoord(fileName, path):
    xyz = readNumPyScan(fileName, path)
    return np.mean(xyz,axis=0)




