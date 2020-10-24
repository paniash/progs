import matplotlib.pyplot as plt
import numpy as np

rho = 10
R = 5
x = np.linspace(0, 21, 1000)
for a in range(1,5):
    y = rho/(1 + np.exp((x-R)/a))
    plt.title("Variation in $a$")
    plt.plot(x, y, label=f'a={a}')
    plt.legend()

plt.show()
