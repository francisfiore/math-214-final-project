import numpy as np
import matplotlib.pyplot as plt
from imageio import imread
import math
import sys
import os


im = imread("neri.jpeg", as_gray=True)
trans = np.fft.fft2(im)
trans = np.log10(abs(trans)); 
plt.imshow(trans);
plt.show()

sys.exit()

t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real, freq, sp.imag)
plt.show()