import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Setup the data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
point, = ax.plot([], [], 'ro') # The moving 'dot'

# 2. The 'Body' of the loop (Update function)
def update(frame):
    # 'frame' acts as our loop index (i)
    point.set_data([x[frame]], [y[frame]])
    return point,

# 3. Running the animation (The 'For' Loop)
# frames=100 is essentially: for frame in range(100)
ani = FuncAnimation(fig, update, frames=len(x), interval=20, blit=True)

plt.show()