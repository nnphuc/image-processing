import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0338(a)(blurry_moon).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)


laplacian = 1.0/16*np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]],dtype=np.float)

img_blur = skimage.filters.edges.convolve(img,laplacian,mode="constant")

alpha = [0.2,1.0,2.5]



fig = plt.figure(figsize=(8,6),dpi=100)
plt.subplot(221)
plt.imshow(img, cmap="gray")

for i in range(3):
    out = img + alpha[i]*(img-img_blur)
    plt.subplot(2,2,i+2)
    plt.imshow(out,cmap="gray")

plt.show()


