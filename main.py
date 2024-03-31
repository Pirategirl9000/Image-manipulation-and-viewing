import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

def alter(arr, start, end):
    for x in arr:
        for pixel in x:
            if (pixel[0] > 140) and (pixel[1] > 140) and (pixel[2] > 140):
                arr[x, pixel] = [0, 255, 0]
        start += 1
        if (start >= end):
            return arr


im = io.imread('IMG_1023.jpg')
imarr=np.array(im)

size = imarr.size
print(imarr.shape)

whitish_pixels = np.count_nonzero((imarr[ :, :, 0] > 140) & (imarr[ :, :, 1] > 140) & (imarr[ :, :, 2] > 140)) * 3

print(f"{whitish_pixels} out of {size} pixels are whitish")
print(f"{whitish_pixels / size * 100}% of the image is whitish")

fraction = np.shape[0] / 10

for i in range(9):
    imarr = alter(imarr, i*fraction, (i+1)*fraction)




#for x in imarr: #x index
#    for y in x:
#        if (y[0] > 140) and (y[1] > 140) and (y[2] > 140):
#            imarr[x, y] = [255, 0, 0]

        

plt.imshow(imarr)
plt.show()