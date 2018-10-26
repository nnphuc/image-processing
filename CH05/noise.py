import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np
import math
import sys

FILE_NAME = "Fig0503 (original_pattern).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-4]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)

f,axs = plt.subplots(2,4)

def disable_tick(axs):
    for u in range(len(axs)):
        for v in range(len(axs[0])):
            axs[u,v].axes.get_xaxis().set_ticks([])
            axs[u,v].axes.get_yaxis().set_ticks([])

disable_tick(axs)

axs[0,0].imshow(img,cmap="gray")
axs[0,0].set_title("original")
axs[1,0].hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

mean = 0
sigma = 0.1
img2 = img + np.random.normal(mean,sigma, img.shape)
axs[0,1].imshow(img2,cmap="gray")
axs[0,1].set_title("original")
axs[1,1].hist(img2.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

img3 = img+np.random.rayleigh(0.1,img.shape)
axs[0,2].imshow(img3,cmap="gray")
axs[0,2].set_title("original")
axs[1,2].hist(img3.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

img4 = img
amount = 0.1
img4[np.random.uniform(0.0,1.0,img.shape)<amount]=1
axs[0,3].imshow(img4,cmap="gray")
axs[0,3].set_title("original")
axs[1,3].hist(img4.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')



plt.savefig("output/"+sys.argv[0][:-2]+"png")
plt.show()

