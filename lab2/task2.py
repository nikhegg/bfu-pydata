from PIL import Image

rt = gt = bt = 0
def updateColorAmount(colors):
    global rt, gt, bt
    r, g, b = colors
    colors = {"r": r, "g": g, "b": b}
    maxValue = max(colors.values())
    for color, value in colors.items():
        if value == maxValue:
            if color == "r":
                rt += 1
            elif color == "g":
                gt += 1
            elif color == "b":
                bt += 1

with Image.open("rgbimg.jpg") as image:
    width, height = image.size
    for x in range(width):
        for y in range(height):
            updateColorAmount(image.getpixel((x,y)))

# Будем также учитывать, что R может быть равно G и другие случаи
# Поэтому лучше сначала собрать названия, а потом вывести через split
colors = {"красный": rt, "зелёный": gt, "синий": bt}
primeColors = []
maxValue = max(colors.values())
for color, value in colors.items():
    if value == maxValue:
        primeColors.append(color)
resString = ' и '.join(primeColors)
print(f"Преобладающий цвет: {resString}")