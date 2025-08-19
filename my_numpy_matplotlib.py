import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

#نمودار اول
y1 = x**3

plt.figure(figsize=(6, 4))
plt.plot(x, y1, 'b--', label='x^3')
plt.fill_between(x, y1, color='lightblue')
plt.title('plot of x^3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

#نمودار دوم
y2 =np.cos(1.2*x)
y3 = np.exp(-(x**2))

plt.figure(figsize=(6, 4))
plt.plot(x, y2,'g--', label='cos(1.2x)')
plt.plot(x, y3, 'r', label='exp(-x^2)')
plt.title('plot of mathematical functions')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()