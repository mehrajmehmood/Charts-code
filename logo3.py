import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(x, y1, label='sin(x)', color='blue')
axs[0].set_xlabel('X-axis')
axs[0].set_ylabel('Y-axis')
axs[0].set_title('Sine Wave')
axs[0].legend()
axs[1].plot(x, y2, label='cos(x)', color='green')
axs[1].set_xlabel('X-axis')
axs[1].set_ylabel('Y-axis')
axs[1].set_title('Cosine Wave')
axs[1].legend()
plt.tight_layout()
plt.show()