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

img1 = io.imread("input/"+"Fig0508(a)(circuit-board-pepper-prob-pt1).tif")
img1 = skimage.img_as_float(img1)
img2 = io.imread("input/"+"Fig0508(b)(circuit-board-salt-prob-pt1).tif")
img2 = skimage.img_as_float(img2)


f,axs = plt.subplots(2,2,figsize=(12,9))
disable_tick(axs)

axs[0,0].imshow(img1,cmap="gray")
axs[0,0].set_title("pepper noise p=0.1")

axs[0,1].imshow(img2,cmap="gray")
axs[0,1].set_title("salt noise p=0.1")

img3 = F.contraharmonic_mean_filter(img1,3,3,1.5)
axs[1,0].imshow(img3,cmap="gray")
axs[1,0].set_title("a & contraharmonic Q=1.5")

img4 = F.contraharmonic_mean_filter(img2,3,3,-1.5)
axs[1,1].imshow(img4,cmap="gray")
axs[1,1].set_title("b & contraharmonic Q=-1.5")


plt.savefig("output/"+sys.argv[0][:-2]+"png")
plt.show()

