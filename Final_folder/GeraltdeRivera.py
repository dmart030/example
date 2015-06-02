

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft


DataIN = np.loadtxt('official_stuff for_stuff.txt')
y = DataIN[:]
x = np.array([i for i in range(len(y))])
fourier_transform = fft(y)
plt.ylim(-100,50)
plt.plot(x,np.imag(fourier_transform), 'b',label = "imaginary fft plot")
plt.plot(x,np.real(fourier_transform), 'g', label = "real fft plot")
plt.plot(x,y, 'r', label = "Not fft")
plt.legend()
plt.ylabel('Pressure[torr]')
plt.title('Fourier trnasform of the decreasing pressure')
plt.xlabel('Time[s]')
plt.show()