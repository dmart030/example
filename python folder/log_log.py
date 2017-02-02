from pylab import *
import matplotlib.pyplot as pyplot

axis = [ 5.79, 10.8, 15, 22.8, 77.8, 143, 287, 450, 590 ]
Period = [0.241, 0.615, 1, 1.88, 11.9, 29.5, 84, 165, 248]
P2_over_axis = [2.99, 3, 2.96, 2.98, 3.01, 2.98, 2.99, 2.99]
b = []
fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)

line, = ax.plot(axis, Period, color='blue', lw=2)


ax.set_yscale('log')
ax.set_xscale('log')
ax.grid(b = True, which = 'major', color = 'b', linestyle = '-')
ax.grid(b = True, which = 'minor', color = 'b', linestyle = '-')
print('y = ax^b is the same as showing log(y) = log(a) + blog(x)')
for i in range((len(axis))):
    b.append((Period[i]**2)/(axis[i]**3))
print(b)
show()


