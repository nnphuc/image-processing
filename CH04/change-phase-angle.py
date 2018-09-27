import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np
import cmath
import math


FILE_NAME = "Fig0429(a)(blown_ic).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-4]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)

fft = np.fft.fft2(img)

r = np.abs(fft)
angle = np.angle(fft)

angle1 = angle*.5
angle2 = angle*.25

img2 = np.abs(np.real(np.fft.ifft2(r*(np.cos(angle1)+1j*np.sin(angle1)))))
img3 = np.abs(np.real(np.fft.ifft2(r*(np.cos(angle2)+1j*np.sin(angle2)))))

img2/=np.max(img2)
img3/=np.max(img3)
img2 = np.log(img2*256+1)
img3 = np.log(img3*256+1)






plt.figure(1)
plt.subplot(131)
plt.imshow(img, cmap="gray")
plt.subplot(132)
plt.imshow(img2, cmap="gray")
plt.subplot(133)
plt.imshow(img3, cmap="gray")

plt.show()

io.imsave(OUTPUT_FILE,img3)

