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

fraction = np.shape(imarr)
fraction = fraction[0]
fraction /= 16
fraction = int(fraction)

def alter(start, end):
    current_row = int(start)
    start = int(start)
    end = int(end)
    global imarr

    while (current_row < end):
        i = 0
        while (i < 3024):
            if (imarr[current_row, i, 0] > 140) and (imarr[current_row, i, 1] > 140 and (imarr[current_row, i, 2] > 140)):
                imarr[current_row, i] = [0, 255, 0]
            i += 1
        current_row += 1


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


plt.imshow(imarr, vmin = 250)
plt.show()