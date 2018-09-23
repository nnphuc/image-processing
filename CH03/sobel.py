import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0342(a)(contact_lens_original).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)


kernel = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]],dtype=np.float)
print("kernel",kernel)

sobel1 = skimage.filters.edges.convolve(img,kernel,mode="constant")

sobel2 = skimage.filters.edges.convolve(img,kernel.T,mode="constant")

out = np.abs(sobel1) + np.abs(sobel2)
out/=np.max(out)


plt.figure(1)
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.subplot(122)
plt.imshow(out, cmap="gray")
plt.show()

io.imsave(OUTPUT_FILE,out)

