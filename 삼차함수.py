import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = y = x**3 - 3*x

plt.plot(x, y)
plt.grid(True)
plt.show()
