import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0309(a)(washed_out_aerial_image).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)

c = 1.0
img_3 = c*np.power(img, np.full(img.shape, 3.0))
img_4 = c*np.power(img, np.full(img.shape, 4.0))
img_5 = c*np.power(img, np.full(img.shape, 5.0))

plt.figure(1)
plt.subplot(221)
plt.imshow(img, cmap="gray")
plt.subplot(222)
plt.imshow(img_3,cmap="gray")
plt.subplot(223)
plt.imshow(img_4,cmap="gray")
plt.subplot(224)
plt.imshow(img_5,cmap="gray")

plt.show()


