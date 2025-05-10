import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 300)

y = np.log2(x)

plt.plot(x, y)
plt.grid(True)
plt.show()