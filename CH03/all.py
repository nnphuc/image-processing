import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0343(a)(skeleton_orig).tif"
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

lap = np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]])

sobel_ker = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]])

def sobel(img):

    s1 = skimage.filters.edges.convolve(img,sobel_ker,mode="constant")
    s2 = skimage.filters.edges.convolve(img,sobel_ker.T,mode="constant")
    out = np.abs(s1)+np.abs(s2)
    return out
"""
plot
1 2 3 4
5 6 7 8

1: origin image
2: laplacian of 1
3: 1+2
4: sobel of 1
5: 5x5 average filter of 4
6: 3*5
7: 1+6
8: power scale of 7
"""
fig = plt.figure()


plt.subplot(241)
plt.imshow(img,cmap="gray")
plt.axis("off")


img_lap = skimage.filters.edges.convolve(img,lap,mode="constant")
img_lap=np.abs(img_lap)
plt.subplot(242)
plt.imshow(img_lap,cmap="gray")
plt.axis("off")

img_3 = img+img_lap
plt.subplot(243)
plt.imshow(img_3,cmap="gray")
plt.axis("off")

img_4 = sobel(img)
plt.subplot(244)
plt.imshow(img_4,cmap="gray")
plt.axis("off")


k = np.ones((5,5))
k/=np.sum(k)

img5 = skimage.filters.edges.convolve(img_4, k,mode="constant")

plt.subplot(245)
plt.imshow(img5,cmap="gray")
plt.axis("off")

img6 = img_3*img5
plt.subplot(246)
plt.imshow(img5,cmap="gray")
plt.axis("off")

img7 = img+img6
plt.subplot(247)
plt.imshow(img7,cmap="gray")
plt.axis("off")


img8= img7

img8 = np.power(img8,np.full(img8.shape, 0.3))
plt.subplot(248)
plt.imshow(img8,cmap="gray")
plt.axis("off")


plt.show()


