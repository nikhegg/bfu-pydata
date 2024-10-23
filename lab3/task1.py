from os import path as pth, listdir as listdir
from sys import argv
from skimage import io, transform, color, util
from pathlib import Path

def byte_image(img):
    return util.img_as_ubyte(img)


def rotate_image(img, ang = 90):
    return byte_image(transform.rotate(img, ang))

def invert_image(img):
    return byte_image(util.invert(img))

def resize_image(img, width = 64, height = 64):
    return byte_image(transform.resize(img, ([width, height])))

def monochrome_image(img):
    return byte_image(color.rgb2gray(img))

def swirl_image(img, strength = 50):
    return byte_image(transform.swirl(img, strength=strength))

def destroy_image(img): # Complex Transformation
    img = swirl_image(img, 100)
    img = invert_image(img)
    img = rotate_image(img, 180)
    img = resize_image(img)
    img = resize_image(img, 256, 256)
    return img

actions = {
    "rotate": rotate_image,
    "invert": invert_image,
    "resize": resize_image,
    "monochrome": monochrome_image,
    "swirl": swirl_image,
    "destroy": destroy_image
}


params = argv
params.pop(0)

transformation = None
transformArg = None
path = None
flag = None
for i in range(0, len(params)):
    param = params[i]
    if param == "--path":
        flag = 1
    elif flag == 1:
        path = param
        flag = None
    elif flag == 2:
        transformArg = param
    else:
        transformation = param[2:]
        flag = 2


def main():
    if not transformation in actions:
        print("No such transformation")
        return
    folder = Path(path)
    files = sorted(folder.glob('*.jpg'))
    for file in files[20:]: # Только первые 20 файлов
        file.unlink()

    for file in listdir(path):
        relpath = pth.join(path, file)
        action = actions.get(transformation)
        img = io.imread(relpath)
        if transformArg != None:
            img = action(img, float(transformArg))
        else:
            img = action(img)
        io.imsave(f"{path}/t-{file}", img)

main()