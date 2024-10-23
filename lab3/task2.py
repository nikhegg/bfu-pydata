from sys import argv
from PIL import Image as PImage
from matplotlib import pyplot as Pyplot
from skimage import io, exposure

COLOR_RED="#FF0000"
COLOR_GREEN="#00FF00"
COLOR_BLUE="#0000FF"

params = argv
params.pop(0)

path = None
flag = None
for i in range(0, len(params)):
    param = params[i]
    if param == "--path":
        flag = 1
    elif flag == 1:
        path = param
        flag = None

fig, axs = Pyplot.subplots(4,2)

axs[0,0].axis("off")
axs[1,0].axis("off")
axs[2,0].axis("off")
axs[3,0].axis("off")

# Pillow
with PImage.open(path) as image:
    axs[0,0].imshow(image)
    axs[0,0].set_title("Source")

    histo = image.histogram()
    axs[0,1].plot(histo[0:256], color=COLOR_RED)
    axs[0,1].plot(histo[256:512], color=COLOR_GREEN)
    axs[0,1].plot(histo[512:], color=COLOR_BLUE)
    axs[0,1].set_title("Histogram")
    
# Sci-kit
scimage = io.imread(path)
r, g, b = scimage[:, :, 0], scimage[:, :, 1], scimage[:, :, 2]
r_hist, r_bins = exposure.histogram(r)
axs[1,1].plot(r_bins, r_hist, color=COLOR_RED)
axs[1,1].set_title("R-Histo")
g_hist, g_bins = exposure.histogram(g)
axs[2,1].plot(g_bins, g_hist, color=COLOR_GREEN)
axs[2,1].set_title("G-Histo")
b_hist, b_bins = exposure.histogram(b)
axs[3,1].plot(b_bins, b_hist, color=COLOR_BLUE)
axs[3,1].set_title("B-Histo")

Pyplot.tight_layout()
Pyplot.savefig("histo.jpg")
Pyplot.show()