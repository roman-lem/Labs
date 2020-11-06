import numpy as np
import math

x = np.array([0.59, 0.79, 0.93, 1.65, 2.72])
y = np.array([0.00547, 0.00644, 0.00697, 0.01032, 0.01914])

x2 = np.array([1.07, 1.40, 1.90, 2.74, 4.29])
y2 = np.array([0.01355, 0.01715, 0.02007, 0.02778, 0.03430])

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

z2 = np.polyfit(x2, y2, 1)
p2 = np.poly1d(z2)

print("I1 = ", end = "")
print((p(1) - p(0))/1)

print("M0 = ", end = "")
print(p(0))

print("I2 = ", end = "")
print((p2(1) - p2(0))/1)

print("M1 = ", end = "")
print(p2(0))

sigma = 0;
for i in range(4):
	sigma += ((p(1) - p(0))/1 - y[i+1]/x[i+1]) * ((p(1) - p(0))/1 - y[i+1]/x[i+1])

print(math.sqrt(sigma/5))

sigma = 0;
for i in range(4):
	sigma += ((p2(1) - p2(0))/1 - (y2[i+1] - y2[0])/(x2[i+1] - x2[0])) * ((p2(1) - p2(0))/1 - (y2[i+1] - y2[0])/(x2[i+1] - x2[0]))

print(math.sqrt(sigma/5))

#plotting
import matplotlib.pyplot as plt
xp = np.linspace(0.5, 4.5, 1000)

plt.plot(x, y, '+', color = 'r')
plt.plot(xp, p(xp), color = 'k', label = "r = 9mm")

plt.plot(x2, y2, '*', color = 'b')
plt.plot(xp, p2(xp), color = 'm', label = "r = 17,5mm")

plt.xlabel('β, 1/c^2')
plt.ylabel('M, 10^-3 Нм')

plt.legend()

plt.show()