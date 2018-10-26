import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np
import math
import sys


def disable_tick(axs):
    for u in range(len(axs)):
            axs[u].axes.get_xaxis().set_ticks([])
            axs[u].axes.get_yaxis().set_ticks([])

def disc(r):
    r2 = r//2
    t = np.fromfunction(lambda x,y: (x-r2)**2+(y-r2)**2 <=r2**2,(r,r))
    w = np.zeros((r,r))
    w[t]=1
    return w


def erode(A,B):
    """
    A (-) B = {z| Bz & Ac==0} 
    """
    k = B.shape[0]//2
    H,W = A.shape
    out = np.empty_like(A)

    for i in range(H):
        for j in range(W):
            dx = max(k-i,0)
            dy = max(k-j,0)
            #complement of A
            window = 1-A[max(0,i-k):min(H,i+k+1),max(0,j-k):min(W,j+k+1)]
            t = np.zeros(B.shape)
            t[dx:dx+window.shape[0],dy:dy+window.shape[1]] = window
            if np.sum(t*B) ==0:
                out[i,j]=1
            else:
                out[i,j]=0
    return out

def dialate(A,B):
    """
    A (-) B = {z| Bz & Ac==0} 
    """
    k = B.shape[0]//2
    H,W = A.shape
    out = np.empty_like(A)
    Bz = B[::-1,::-1]

    for i in range(H):
        for j in range(W):
            dx = max(k-i,0)
            dy = max(k-j,0)
            #complement of A
            window = A[max(0,i-k):min(H,i+k+1),max(0,j-k):min(W,j+k+1)]
            t = np.zeros(Bz.shape)
            t[dx:dx+window.shape[0],dy:dy+window.shape[1]] = window
            if np.sum(t*Bz) !=0:
                out[i,j]=1
            else:
                out[i,j]=0
    return out
#duality
def dialate1(A,B):
    return 1-erode(1-A,B[::-1,::-1])

img1 = io.imread("input/"+"Fig0907(a)(text_gaps_1_and_2_pixels).tif")
img1 = skimage.img_as_float(img1)

f,axs = plt.subplots(1,2,figsize=(12,9))
disable_tick(axs)

axs[0].imshow(img1,cmap="gray")
axs[0].set_title("original")

d = np.array([
    [0,1,0],
    [1,1,1],
    [0,1,0]])
img2 = dialate1(img1,d)
axs[1].imshow(img2,cmap="gray")
axs[1].set_title("dialation")

plt.savefig("output/"+sys.argv[0][:-2]+"png")
plt.show()


