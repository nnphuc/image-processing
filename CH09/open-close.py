import skimage
from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import tifffile


def disable_tick(axs):
    for u in range(len(axs)):
        for v in range(len(axs[0])):
            axs[u,v].axes.get_xaxis().set_ticks([])
            axs[u,v].axes.get_yaxis().set_ticks([])

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
        duality
        (A - B)c = Ac + B^
        (A + B)c = Ac - B^
    """
    Bz = np.flip(np.flip(B,0),1)
    return 1-erode(1-A,Bz)

def Open(A,B):
    return dialate(erode(A,B),B)

def Close(A,B):
    return erode(dialate(A,B),B)

img1 = io.imread("input/"+"Fig0911(a)(noisy_fingerprint).png")
img1 = skimage.img_as_float(img1)

f,axs = plt.subplots(2,2,figsize=(12,9))
disable_tick(axs)

axs[0,0].imshow(img1,cmap="gray")
axs[0,0].set_title("original")

d = np.ones((3,3))

img2 = Open(img1,d)
axs[0,1].imshow(img2,cmap="gray")
axs[0,1].set_title("opening of original")


img3 = dialate(img2,d)
axs[1,0].imshow(img3,cmap="gray")
axs[1,0].set_title("dialation of opening")

img4 = Close(img2,d)
axs[1,1].imshow(img4,cmap="gray")
axs[1,1].set_title("closing of opening")

plt.savefig("output/"+sys.argv[0][:-2]+"png")
plt.show()


