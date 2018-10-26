import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import filters as F


def disable_tick(axs):
    for u in range(len(axs)):
        for v in range(len(axs[0])):
            axs[u,v].axes.get_xaxis().set_ticks([])
            axs[u,v].axes.get_yaxis().set_ticks([])

def butterworth_bandreject(h,w,D0,W,n=2):
    
    def D(x,y):
        d = np.sqrt((x-h//2)**2 + (y-w//2)**2)
        return 1/(1+(d*W/(1e-15+np.abs(d**2-D0**2)))**(2*n))
    
    return np.fromfunction(D,(h,w))

img1 = io.imread("input/"+"Fig0516(a)(applo17_boulder_noisy).tif")

f,axs = plt.subplots(2,2,figsize=(12,9))
disable_tick(axs)

axs[0,0].imshow(img1,cmap="gray")
axs[0,0].set_title("sinsusoidal noise")

fft = np.fft.fft2(img1)
fft = np.fft.fftshift(fft)
img2 = np.abs(fft)
img2 = np.log(img2)
axs[0,1].imshow(img2,cmap="gray")
axs[0,1].set_title("fourier transform")

img3=butterworth_bandreject(img1.shape[0],img1.shape[1],176,8)
axs[1,0].imshow(img3,cmap="gray")
axs[1,0].set_title("butterworth bandreject")
 
fft1 = fft*img3
img4 = np.fft.ifft2(fft1)
img4 = np.abs(img4)
img4/=np.max(img4)
axs[1,1].imshow(img4,cmap="gray")
axs[1,1].set_title("result")


plt.savefig("output/"+sys.argv[0][:-2]+"png")
plt.show()


