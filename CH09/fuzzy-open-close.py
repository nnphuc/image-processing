import numpy as np
import skimage
from skimage import io,filters,color
import matplotlib.pyplot as plt


def get_window(img, x, y, b):
    h, w = b.shape
    w2 = w//2
    h2 = h//2
    minx = max(0, x-w2)
    maxx = min(img.shape[1],x+w2+1)
    miny = max(0, y-h2)
    maxy = min(img.shape[0],y+h2+1)
    img_slice = img[miny:maxy,minx:maxx]
    dx = w2 - (x-minx)
    dy = h2 - (y-miny)
    b_slice = b[dy:(dy+img_slice.shape[0]),dx:(dx+img_slice.shape[1])]
    
    return img_slice, b_slice

def erode(img, b):
    out = np.empty_like(img)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            u,v = get_window(img, x, y, b)
            
            out[y,x] = np.amin(u-v)
            
    return out

def dialate(img, b):
    out = np.empty_like(img)
    bz = np.flip(np.flip(b,1),0)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            u,v = get_window(img, x, y, b)
            
            out[y,x] = np.amax(u+v)
                   
    return out

def opening(img,b):
    return dialate(erode(img,b),b)

def closing(img,b):
    return erode(dialate(img,b),b)

def disc(r):
    r2 = r//2
    t = np.fromfunction(lambda x,y: (x-r2)**2+(y-r2)**2 <=r2**2,(r,r))
    w = np.zeros((r,r))
    w[t]=1
    return w

img = io.imread("input/Fig0935(a)(ckt_board_section).tif")
img = skimage.img_as_float(img)

d3 = disc(3*2+1)*0.2
d5 = disc(5*2+1)*0.2
f,axs = plt.subplots(1,3,figsize=(12,9))   

axs[0].imshow(img,cmap="gray")
axs[1].imshow(opening(img,d3),cmap="gray")
axs[2].imshow(closing(img,d5),cmap="gray")   
plt.show()
