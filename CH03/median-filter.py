import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np


FILE_NAME = "Fig0335(a)(ckt_board_saltpep_prob_pt05).tif"
INPUT_FILE = "input/"+FILE_NAME
OUTPUT_FILE = "output/"+FILE_NAME[:-3]+".png"

img = io.imread(INPUT_FILE)


def median(img):
    out = img.copy()

    for i in range(1,out.shape[0]-1):
        for j in range(1,out.shape[1]-1):
            window = img[i-1:i+1,j-1:j+1]
            out[i,j] = np.median(window)
    return out

img_out = median(img)



plt.figure(1)
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.subplot(122)
plt.imshow(img_out, cmap="gray")
plt.show()

io.imsave(OUTPUT_FILE,img_out)

