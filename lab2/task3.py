from PIL import Image, ImageDraw,ImageFont

with Image.open("rgbimg.jpg") as image:
    width, height = image.size
    sizeBase = width/height

    with Image.open("bfulogo.png") as watermark:
        watermarkSize = int(46 * sizeBase)
        watermark = watermark.resize((watermarkSize, watermarkSize))
        _, _, _, mask = watermark.split()
        mask.putalpha(150)
        image.paste(watermark, (width - watermarkSize - 10, height - watermarkSize - 10), mask)

    # В документации ничего не сказано про использование .truetype с with или try
    # https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#example-draw-a-gray-cross-over-an-image
    fontSize = int(28 * sizeBase)
    arial = ImageFont.truetype("arial.ttf", fontSize)

    draw = ImageDraw.Draw(image)
    draw.text([5, height - fontSize - 10], "БФУ", fill=(0,0,0,255), font=arial)
    image.show()

    filename = image.filename.split(".")
    filename.pop()
    filename = ".".join(filename)
    image.save(f"{filename}-wm.jpg", "JPEG")