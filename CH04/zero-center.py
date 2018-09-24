import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0429(a)(blown_ic).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)

img2 = np.fft.fft2(img)
img2 = np.fft.fftshift(img2)
img2[img2.shape[0]//2,img2.shape[1]//2]=0

img2 = np.fft.ifft2(img2)

img2 = np.abs(img2)
img2/=np.max(img2)

plt.figure()
plt.subplot(121)
plt.imshow(img,cmap="gray")

plt.subplot(122)
plt.imshow(img2,cmap="gray")
plt.show()

io.imsave(OUTPUT_FILE,img2)
