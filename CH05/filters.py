import numpy

def arithmetic_mean_filter(img,w,h):
    w2 = w//2
    h2 = h//2

    out = img.copy()
    for i in range(h2,img.shape[0]-h2):
        for j in range(w2,img.shape[1]-w2):
            window = img[i-h2:i+h2+1,j-w2:j+w2+1]
            out[i,j] = numpy.sum(window)/(w*h)
    return out

def geometric_mean_filter(img,w,h):
    w2 = w//2
    h2 = h//2

    out = img.copy()
    for i in range(h2,img.shape[0]-h2):
        for j in range(w2,img.shape[1]-w2):
            window = img[i-h2:i+h2+1,j-w2:j+w2+1]
            out[i,j] = numpy.prod(numpy.power(1e-4+window,1/w/h))
    return out

def harmonic_mean_filter(img,w,h):
    w2 = w//2
    h2 = h//2
    out = img.copy()
    for i in range(h2,img.shape[0]-h2):
        for j in range(w2,img.shape[1]-w2):
            window = img[i-h2:i+h2+1,j-w2:j+w2+1]
            out[i,j] = w*h/(numpy.sum(1/window))
    return out

def contraharmonic_mean_filter(img,w,h,q):
    w2 = w//2
    h2 = h//2
    out = img.copy()
    for i in range(h2,img.shape[0]-h2):
        for j in range(w2,img.shape[1]-w2):
            window = img[i-h2:i+h2+1,j-w2:j+w2+1]
            window[window<1e-9]=1e-9
            out[i,j] = numpy.sum(numpy.power(window,q+1))/(numpy.sum(numpy.power(window,q)))
    return out



def median_filter(img,w,h):
    w2 = w//2
    h2 = h//2

    out = img.copy()
    for i in range(h2,img.shape[0]-h2):
        for j in range(w2,img.shape[1]-w2):
            window = img[i-h2:i+h2+1,j-w2:j+w2+1]
            out[i,j] = numpy.median(window)
    return out

def max_filter(img,w,h):
    w2 = w//2
    h2 = h//2

    out = img.copy()
    for i in range(h2,img.shape[0]-h2):
        for j in range(w2,img.shape[1]-w2):
            window = img[i-h2:i+h2+1,j-w2:j+w2+1]
            out[i,j] = numpy.max(window)
    return out

def min_filter(img,w,h):
    w2 = w//2
    h2 = h//2

    out = img.copy()
    for i in range(h2,img.shape[0]-h2):
        for j in range(w2,img.shape[1]-w2):
            window = img[i-h2:i+h2+1,j-w2:j+w2+1]
            out[i,j] = numpy.min(window)
    return out

def midpoint_filter(img,w,h):
    w2 = w//2
    h2 = h//2

    out = img.copy()
    for i in range(h2,img.shape[0]-h2):
        for j in range(w2,img.shape[1]-w2):
            window = img[i-h2:i+h2+1,j-w2:j+w2+1]
            out[i,j] = 0.5*(numpy.max(window)+numpy.min(window))
    return out

def alpha_trimmed_filter(img,w,h,d):
    w2 = w//2
    h2 = h//2

    out = img.copy()
    for i in range(h2,img.shape[0]-h2):
        for j in range(w2,img.shape[1]-w2):
            window = img[i-h2:i+h2+1,j-w2:j+w2+1]
            out[i,j] = numpy.sum(window)/(w*h-d)
    return out

def adaptive_median_filter(img,S):
    def get_window(img,x,y,w,h):

        return img[x-w:x+w+1,y-h:y+h+1]

    def solve(x,y):
        ww = [1,0]
        nxt = 1
        while ww[1]<=S:
            w,h=ww
            if  x-w<=0 or x+w>=img.shape[0] or y-h<=0 or y+h>=img.shape[1]:
                return img[x,y]
            window = get_window(img,x,y,w,h)
            zxy =  img[x,y]
            zmin = numpy.min(window)
            zmax = numpy.max(window)
            zmed = numpy.median(window)
            A1 = zmed - zmin
            A2 = zmed - zmax
            if A1 > 0 and A2 < 0:
                break
            if h>=S:
                return zmed
            ww[nxt]+=1
            nxt = (nxt+1)%2

        B1 = zxy - zmin
        B2 = zxy - zmax
        if B1 > 0 and B2 < 0:
            return zxy
        else:
            return zmed
    out = numpy.empty_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i,j] = solve(i,j)
    return out
