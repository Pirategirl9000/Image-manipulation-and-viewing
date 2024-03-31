import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
import threading

im = io.imread('IMG_1023.jpg')
imarr=np.array(im)

size = imarr.size
print(imarr.shape)

whitish_pixels = np.count_nonzero((imarr[ :, :, 0] > 140) & (imarr[ :, :, 1] > 140) & (imarr[ :, :, 2] > 140)) * 3

print(f"{whitish_pixels} out of {size} pixels are whitish")
print(f"{whitish_pixels / size * 100}% of the image is whitish")

fraction = np.shape(im)[0] / 16

#for i in range(15):
#    print(f"Starting {i} sweep")
#    imarr = alter(imarr, i*fraction, (i+1)*fraction-1)

def alter(start, end):
    current = int(start)
    start = int(start)
    end = int(end)
    global imarr
    amount = end - start
    arr = []
    arr.append(imarr[start:end-1])

    for row in arr[0]:
        for pixel in row:
            if (pixel[0] > 140) and (pixel[1] > 140) and (pixel[2] > 140):
                arr[current, pixel] = [0, 255, 0]
        start += 1
        if (start % 20 == 0):
            print(f"{end - current} left out of {amount}")
        if (current >= end):
            print("complete")
            imarr[start:end-1] = arr
            return

threads = [
    threading.Thread(target=alter, args=(0, fraction - 1)),
    threading.Thread(target=alter, args=(fraction, (fraction * 2) - 1)),
    threading.Thread(target=alter, args=((fraction * 2), (fraction * 3) - 1)),
    threading.Thread(target=alter, args=((fraction * 3), (fraction * 4) - 1)),
    threading.Thread(target=alter, args=((fraction * 4), (fraction * 5) - 1)),
    threading.Thread(target=alter, args=((fraction * 5), (fraction * 6) - 1)),
    threading.Thread(target=alter, args=((fraction * 6), (fraction * 7) - 1)),
    threading.Thread(target=alter, args=((fraction * 7), (fraction * 8) - 1)),
    threading.Thread(target=alter, args=((fraction * 8), (fraction * 9) - 1)),
    threading.Thread(target=alter, args=((fraction * 9), (fraction * 10) - 1)),
    threading.Thread(target=alter, args=((fraction * 10), (fraction * 11) - 1)),
    threading.Thread(target=alter, args=((fraction * 11), (fraction * 12) - 1)),
    threading.Thread(target=alter, args=((fraction * 12), (fraction * 13) - 1)),
    threading.Thread(target=alter, args=((fraction * 13), (fraction * 14) - 1)),
    threading.Thread(target=alter, args=((fraction * 14), (fraction * 15) - 1)),
    threading.Thread(target=alter, args=((fraction * 15), (fraction * 16) - 1)),
           ]

for x in threads:
    print(f"starting thread {x}")
    x.start()

for x in threads:
    x.join()

#for x in imarr: #x index
#    for y in x:
#        if (y[0] > 140) and (y[1] > 140) and (y[2] > 140):
#            imarr[x, y] = [255, 0, 0]


plt.imshow(imarr)
plt.show()