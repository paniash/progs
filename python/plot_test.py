# Importing necessary libraries and modules with conventions
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

# writing a script in OO style
fig, ax = plt.subplots()
ax.plot(x, x, label = 'linear')
ax.plot(x, x**2, label = 'quadratic')
ax.plot(x, x**3, label = 'cubic')
ax.plot(x, np.cos(x), label = 'cosine')
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_title('A simple graph')
ax.legend()

plt.show()

