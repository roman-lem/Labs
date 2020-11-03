import numpy as np

x = np.array([0, 0.0285, 0.061, 0.084, 0.110])
y = np.array([0, 0.192, 0.384, 0.576, 0.749])

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print(p(0.05)/0.05)

#plotting
import matplotlib.pyplot as plt
xp = np.linspace(0, 0.12, 100)
plt.plot(x, y, '.', xp, p(xp))

plt.xlabel('φ, рад')
plt.ylabel('M, Нм')

plt.show()