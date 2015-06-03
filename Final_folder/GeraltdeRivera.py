

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft


DataIN = np.loadtxt('official_stuff for_stuff.txt')
y = DataIN[:]
x = np.array([i for i in range(len(y))])
fourier_transform = fft(y)
plt.ylim(-100,50)
plt.plot(x,y, 'r', label = "f(x)")
plt.legend()
plt.ylabel('Pressure[torr]')
plt.title('our meauremments')
plt.xlabel('Time[s]')
plt.show()