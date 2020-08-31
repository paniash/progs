import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)

fig, ax = plt.subplots()
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label='cubic')
ax.set_xlabel('$X$ axis')
ax.set_ylabel('$Y$ axis')
ax.set_title('Simple plot')
ax.legend()

plt.show()
