import numpy as np
import matplotlib.pyplot as plt

c = 299792458
a = 22.86E-3
steps = 1000
lower = 8E9
upper = 12E9
x = np.linspace(lower,upper,steps)
y = c/np.sqrt((1-(c/(2*a*x))**2))
y2 = np.full(steps,c)
xvert = np.full(100, 6557140376)
yvert = np.linspace(0,1.5E10,100)

# x_meas = [8.91E9]
# y_meas = [442787533.4]
# plt.plot(x_meas,y_meas,color='g',label='measured')

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='r', label=r'$v_p(f)$')
plt.plot(x, y2, color='b',label=r'c')
# plt.plot(xvert,yvert,color='black', label='formula cutoff')
plt.xlabel('Frequency (Hz)')
plt.ylabel('velocity (m/s)')
plt.legend()
plt.grid(True)
plt.show()