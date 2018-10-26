import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import filters as F


def disable_tick(axs):
    for u in range(len(axs)):
        for v in range(len(axs[0])):
            axs[u,v].axes.get_xaxis().set_ticks([])
            axs[u,v].axes.get_yaxis().set_ticks([])

img1 = io.imread("input/"+"Fig0512(a)(ckt-uniform-var-800).tif")
img1 = skimage.img_as_float(img1)
img2 = io.imread("input/"+"Fig0512(b)(ckt-uniform-plus-saltpepr-prob-pt1).tif")
img2 = skimage.img_as_float(img2)


f,axs = plt.subplots(2,3,figsize=(12,9))
disable_tick(axs)

axs[0,0].imshow(img1,cmap="gray")
axs[0,0].set_title("uniform noise")

axs[0,1].imshow(img2,cmap="gray")
axs[0,1].set_title("add salt & pepper noise")


img3 = F.arithmetic_mean_filter(img2,5,5)
axs[0,2].imshow(img3,cmap="gray")
axs[0,2].set_title("arithmetic mean filter")

img4 = F.geometric_mean_filter(img2,5,5)
axs[1,0].imshow(img4,cmap="gray")
axs[1,0].set_title("geometric mean filter")


img5 = F.median_filter(img2,5,5)
axs[1,1].imshow(img5,cmap="gray")
axs[1,1].set_title("median filter")

img6 = F.alpha_trimmed_filter(img2,5,5,5)
axs[1,2].imshow(img6,cmap="gray")
axs[1,2].set_title("alpha trimmed filter")

plt.savefig("output/"+sys.argv[0][:-2]+"png")
plt.show()

