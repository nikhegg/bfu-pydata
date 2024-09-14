from PIL import Image
from os import listdir
from sys import argv


params = argv
params.pop(0)

extension = None
flag = None
for i in range(0, len(params)):
    param = params[i]
    if param == "--ftype":
        flag = 1
    elif flag == 1:
        extension = param
        flag = None

if extension == None:
    raise BaseException("No --ftype parameter specified")

for filename in listdir("."):
    filenameCopy = filename
    fileExt = filenameCopy.split(".").pop()
    if fileExt == extension:
        with Image.open(filename) as image:
            image = image.resize((50, 50))
            image.show()