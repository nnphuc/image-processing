import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np
import math
import sys

FILE_NAME = "Fig0442(a)(characters_test_pattern).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-4]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)

fft = np.fft.fft2(img)
fft = np.fft.fftshift(fft)

def createFilter(H,W,D0):
    def D(y,x):
        d2 =  (y-H/2)**2+(x-W/2)**2
        t = np.exp(-d2/(2*D0**2))
        return t
    return np.fromfunction(D,(H,W))


plt.figure()
plt.subplot(231)

plt.imshow(img,cmap="gray")
i=2
for w,r in enumerate([10,30,60,160,460]):
    t = fft.copy()
    t *= createFilter(t.shape[0],t.shape[1],r)
    im = np.fft.ifft2(t)
    im = np.abs(im)
    plt.subplot(2,3,i)
    plt.title('radius={}'.format(r))
    plt.imshow(im,cmap="gray")
    i+=1

plt.savefig("output/"+sys.argv[0][:-2]+"png")
plt.show()

