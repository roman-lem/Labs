import numpy as np
import math

x = np.array([3.025, 4.225, 5.635, 7.225, 9.025])
y = np.array([4.84, 5.76, 7.29, 9.00, 10.89])

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("k0 = ", end = "")
print((p(4) - p(0))/4)

sigma = 0;
for i in range(5):
	sigma += ((p(4) - p(0))/4 - y[i]/x[i]) * ((p(4) - p(0))/4 - y[i]/x[i])

print(math.sqrt(sigma/5))

#plotting
import matplotlib.pyplot as plt
xp = np.linspace(2, 9.5, 100)
plt.plot(x, y, '.', xp, p(xp))

plt.xlabel('l^2, 10^-3 м^2')
plt.ylabel('T^2, c^2')

plt.show()