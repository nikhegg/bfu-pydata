from os import path, listdir, mkdir
from shutil import copy

def getSmallFiles(dir = ".", maxSize = 2048):
    if not path.isdir(dir):
        return []
    files = listdir(dir)
    result = []
    for f in files:
        filePath = path.join(dir, f)
        if not path.isfile(filePath):
            continue
        if path.getsize(filePath) > maxSize:
            continue
        result.append(f)
    return result

def copyFiles(files = [], fromDir = ".", toDir = "."):
    if fromDir == toDir or len(files) == 0:
        return
    if not path.exists(toDir):
        mkdir(toDir)
    for f in files:
        filePath = path.join(fromDir, f)
        print(f"Copying {filePath} to {toDir}")
        copy(filePath, toDir)


scanPath = str(input("Enter target directory name: "))
while scanPath == "small":
    print(f"/small/ folder is not allowed to copy")
    scanPath = str(input("Enter another target directry name: "))
files = getSmallFiles(scanPath)
if len(files) == 0:
    print("Folder is empty or does not exist")
else:
    print(f"Found {len(files)} files. Copying...")
    copyFiles(files, scanPath, "small")
    print("All files are copied")