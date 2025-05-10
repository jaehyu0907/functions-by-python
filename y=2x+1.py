import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = 2*x+1

plt.plot(x, y)
plt.grid(True)
plt.show()
