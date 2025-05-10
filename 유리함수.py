import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 1000)
y = (3*x+5)/(x-2)

plt.plot(x, y)
plt.grid(True)
plt.show()
