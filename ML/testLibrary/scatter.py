import numpy as np
import matplotlib.pyplot as plt

rng = np.random
rng.rand(50)*10
x = rng.rand(50)*10

y = 2*x+rng.randn(50)

plt.scatter (x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()