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

img1 = io.imread("input/"+"Fig0510(a)(ckt-board-saltpep-prob.pt05).tif")
img1 = skimage.img_as_float(img1)


f,axs = plt.subplots(2,3,figsize=(12,9))
disable_tick(axs)

axs[0,0].imshow(img1,cmap="gray")
axs[0,0].set_title("salt & pepper noise p=0.1")

img2 = F.median_filter(img1,3,3)
axs[0,1].imshow(img2,cmap="gray")
axs[0,1].set_title("median filter 1 times")


img3 = F.median_filter(img2,3,3)
axs[0,2].imshow(img3,cmap="gray")
axs[0,2].set_title("median filter 2 times")

img4 = F.median_filter(img1,3,3)
axs[1,0].imshow(img4,cmap="gray")
axs[1,0].set_title("median filter 3 times")

img5 = io.imread("input/Fig0508(a)(circuit-board-pepper-prob-pt1).tif")
img5 = F.max_filter(img5,3,3)
axs[1,1].imshow(img5,cmap="gray")
axs[1,1].set_title("max filter")

img6 = io.imread("input/Fig0508(b)(circuit-board-salt-prob-pt1).tif")
img6 = F.min_filter(img6,3,3)
axs[1,2].imshow(img6,cmap="gray")
axs[1,2].set_title("min filter")

plt.savefig("output/"+sys.argv[0][:-2]+"png")
plt.show()

