import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from skimage import io


im = io.imread('IMG_1023.jpg')
imarr=np.array(im)

size = imarr.size
imarr[ 255:, :, :] = [255, 255, 255]

whitish_pixels = np.count_nonzero((imarr[ :, :, 0] > 200) & (imarr[ :, :, 1] > 200) & (imarr[ :, :, 2] > 200)) * 3

print(f"{whitish_pixels} out of {size} pixels are whitish")
print(f"{whitish_pixels / size * 100}% of the image is whitish")


plt.imshow(imarr, cmap = 'binary')
plt.show()