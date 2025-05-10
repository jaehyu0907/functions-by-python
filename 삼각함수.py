import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 300)
y = np.cos(x)

plt.plot(x, y)

#xticks = np.arange(-2*np.pi, 2.5*np.pi, np.pi/2)
#xtick_labels = ['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π']
#plt.xticks(xticks, xtick_labels)

plt.grid(True)
plt.show()




