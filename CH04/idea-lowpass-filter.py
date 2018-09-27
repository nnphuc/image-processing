import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0442(a)(characters_test_pattern).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-4]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)

fft = np.fft.fft2(img)
fft = np.fft.fftshift(fft)

def createCircularMask(h, w, center=None, radius=None):

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask

plt.figure()
plt.subplot(231)

plt.imshow(img,cmap="gray")
i=2
for w,r in enumerate([10,30,60,160,460]):
    m = createCircularMask(img.shape[0],img.shape[1],radius=r)
    t = fft.copy()
    t[~m] = 0
    im = np.fft.ifft2(t)
    im = np.abs(im)
    im/=np.max(im)
    plt.subplot(2,3,i)
    plt.title('radius={}'.format(r))
    plt.imshow(im,cmap="gray")
    i+=1

plt.show()
