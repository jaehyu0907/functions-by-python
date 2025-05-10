import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000000)
y = abs(x)

plt.plot(x, y)
plt.grid(True)
plt.show()
