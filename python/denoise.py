import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

img = plt.imread('moonlanding.png')
img_fft = fft.fft2(img)
power = np.abs(img_fft)

pos_mask = np.where(power > 500)
img2 = img_fft.copy()
img2[pos_mask] = 0

filt_img = fft.ifft2(img2)
bower = np.abs(filt_img)

plt.figure()
plt.imshow(bower, plt.cm.gray)
plt.show()
