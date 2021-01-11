import os
def creatrFolder(nameFolder):
    if not (os.path.exists(nameFolder)):
        os.mkdir(nameFolder)

def createScanFolders():
    creatrFolder("Point_EXTR")
    scanList = os.listdir("sourse/Scan")
    for scan in scanList:
        scanDir = scan.split(".")[0]
        path = "Point_EXTR/" + scanDir
        creatrFolder(path)

