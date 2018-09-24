import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0424(a)(rectangle).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)

img2 = np.fft.fft2(img)
img2 = np.fft.fftshift(img2)
img2 = np.abs(img2)


img3 = np.log(1+img2)
img3/=np.max(img3)



plt.figure(1)
plt.subplot(131)
plt.imshow(img, cmap="gray")
plt.subplot(132)
plt.imshow(img2, cmap="gray")
plt.subplot(133)
plt.imshow(img3, cmap="gray")

plt.show()

io.imsave(OUTPUT_FILE,img3)

