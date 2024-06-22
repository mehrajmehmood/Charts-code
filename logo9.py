import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10, 12)
sns.heatmap(data, annot=True, fmt=".1f", linewidths=.5)
plt.title('Heatmap')
plt.show()
