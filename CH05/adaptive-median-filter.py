import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import filters as F


def disable_tick(axs):
    for u in range(len(axs)):
        axs[u].axes.get_xaxis().set_ticks([])
        axs[u].axes.get_yaxis().set_ticks([])

img1 = io.imread("input/"+"Fig0514(a)(ckt_saltpep_prob_pt25).tif")
img1 = skimage.img_as_float(img1)


f,axs = plt.subplots(1,3,figsize=(12,9))
disable_tick(axs)

axs[0].imshow(img1,cmap="gray")
axs[0].set_title("salt & pepper noise")

img2 = F.median_filter(img1,7,7)
axs[1].imshow(img2,cmap="gray")
axs[1].set_title("median filter 7x7")


img3 = F.adaptive_median_filter(img1,3)
axs[2].imshow(img3,cmap="gray")
axs[2].set_title("adaptive median filter")



plt.savefig("output/"+sys.argv[0][:-2]+"png")
plt.show()

