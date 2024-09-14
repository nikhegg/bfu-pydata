from PIL import Image

imgPath = "rgbimg.jpg"

with Image.open(imgPath) as image:
    width, height = image.size

    data = image.getdata()
    r = [(d[0], 0, 0) for d in data]
    g = [(0, d[1], 0) for d in data]
    b = [(0, 0, d[2]) for d in data]

    res = Image.new("RGB", (width * 4, height))
    res.paste(image, (0, 0))

    for i, channel in enumerate([r, g, b]):
        tempimg = Image.new("RGB", (width, height))
        tempimg.putdata(channel)
        res.paste(tempimg, (width * (i+1), 0))

    res.show()