import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0310(b)(washed_out_pollen_image).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)

def histogram(img):
    bins = np.zeros((256,))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            bins[img[i,j]]+=1
    acc = 0.0
    size = np.sum(bins)
    out = np.zeros_like(bins)
    for i in range(len(bins)):
        acc += bins[i]/size
        out[i] = round(acc*256)

    img_hist = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_hist[i,j] = out[img[i,j]]
    return img_hist

img_hist = histogram(img.copy())

plt.figure()
plt.subplot(121)
plt.imshow(img,cmap="gray")
plt.subplot(122)
plt.imshow(img_hist,cmap="gray")
plt.show()

io.imsave(OUTPUT_FILE,img_hist)

