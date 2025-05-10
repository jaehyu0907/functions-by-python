import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 300)

y = x ** 0.5 

plt.plot(x, y)
plt.grid(True)
plt.show()