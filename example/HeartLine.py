
import numpy as np
import matplotlib.pyplot as plt


# a = 1;
# t = np.linspace(0, 2 * np.pi, 1024)
# x = a * (2 * np.cos(t) - np.cos(2*t))
# y = a * (2 * np.sin(t) - np.sin(2*t))
#
#
#
# plt.plot(y, x, color = 'r')      # color 控制心形线的颜色
# plt.show()


t = np.linspace(0, 2 * np.pi, 1024)
plt.axes(polar = True)
plt.plot(t, 1 - np.sin(t))
plt.show()