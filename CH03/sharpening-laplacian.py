import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0338(a)(blurry_moon).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)

kernel = 1.0/9*np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]],dtype=np.float)
img_blur = skimage.filters.edges.convolve(img,kernel,mode="constant")

laplacian = np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]],dtype=np.float)

img_lap = skimage.filters.edges.convolve(img_blur,laplacian,mode="constant")




fig = plt.figure()
plt.subplot(131)
plt.imshow(img, cmap="gray")

plt.subplot(132)
plt.imshow(img_lap,cmap="gray")

out = img + 0.5 * img_lap

plt.subplot(133)
plt.imshow(out,cmap="gray")
plt.show()


