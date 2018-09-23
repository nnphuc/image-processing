import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0335(a)(ckt_board_saltpep_prob_pt05).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)
img = skimage.img_as_float(img)


kernel = 1.0/16*np.array([
    [1,2,1],
    [2,4,2],
    [1,2,1]],dtype=np.float)
print("kernel",kernel)

img_out = skimage.filters.edges.convolve(img,kernel,mode="constant")

plt.figure(1)
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.subplot(122)
plt.imshow(img_out, cmap="gray")
plt.show()

io.imsave(OUTPUT_FILE,img_out)

