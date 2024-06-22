import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Scatter Plot')
plt.show()