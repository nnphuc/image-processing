import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0340(a)(dipxe_text).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)

def gkern(l=5, sig=1.):
    """
    creates gaussian kernel with side length l and a sigma of sig
    """

    ax = np.arange(-l // 2 + 1., l // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)

    kernel = np.exp(-(xx**2 + yy**2) / (2. * sig**2))

    return kernel / np.sum(kernel)

gauss_ker = gkern()

img_blur = skimage.filters.edges.convolve(img,gauss_ker,mode="constant")




fig = plt.figure()
plt.subplot(231)
plt.imshow(img, cmap="gray")

plt.subplot(232)
plt.imshow(img_blur,cmap="gray")

unsharp_mask = (img-img_blur)

plt.subplot(233)
plt.imshow(unsharp_mask,cmap="gray")
img_unsharp_mask = img + 0.5* unsharp_mask

plt.subplot(234)
plt.imshow(img_unsharp_mask,cmap="gray")

lap = np.ones((3,3))
lap = -lap
lap[1,1] = 8
print(lap)

alpha = 0.5
org = np.zeros((3,3))
org[1,1] = 1

print(org)

highboost = org + alpha * lap

img_highboost = skimage.filters.edges.convolve(img,highboost,mode="constant")

#print(np.max(img_highboost),np.min(img_highboost))
#img_highboost/= np.max(img_highboost)

plt.subplot(235)
plt.imshow(img_highboost,cmap="gray")

plt.show()


