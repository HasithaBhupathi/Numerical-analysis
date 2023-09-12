import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

x = np.array([1, 6, 7, 9, 12, 20])

def f(x):
    return math.cos(x)

y = np.array([f(2), f(8), f(6), f(10), f(14),f(41)])

x_interpol = np.linspace(np.min(x), np.max(x), 50)

y_linear = interp1d(x, y,kind="linear")
y_quad = interp1d(x, y, kind="quadratic")
y_cube = interp1d(x, y, kind="cubic")
y_cubicBC = CubicSpline(x, y, bc_type="natural")

plt.plot(x_interpol, y_linear(x_interpol), "Red", label="Linear spline")
plt.plot(x_interpol, y_cube(x_interpol), "blue", label="Cubic spline")
plt.plot(x_interpol, y_quad(x_interpol), "green", label="Quadratic spline")
plt.plot(x_interpol, y_cubicBC(x_interpol), "black", label="CubicBC spline")

#print(y_linear(8))
#print(y_cube(8))
#print(y_quad(8))
#print(y_cubicBC(8))

plt.plot(x, y, "o", label="Data Points")
plt.legend()
plt.show()

#print(x_interpol)
