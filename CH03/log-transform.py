import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0305(a)(DFT_no_log).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)
#img = skimage.img_as_float(img)

c = 1.0
img_log = c * np.log(1.0+img)
img_log /= np.max(img_log)

plt.figure(1)
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.subplot(122)
plt.imshow(img_log, cmap="gray")
plt.show()

io.imsave(OUTPUT_FILE,img_log)

