import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(func, x_0, x_f, y_0, st_sz):

    def rk4(func, x, y, st_sz):
        k0 = st_sz*func(x, y)
        k1 = st_sz*func(x + st_sz/2, y + k0/2)
        k2 = st_sz*func(x + st_sz/2, y + k1/2)
        k3 = st_sz*func(x + st_sz, st_sz + k2)
        return (k0 + 2*k1 + 2*k2 + k3)/6
    x_i = x_0
    y_i = y_0
    X = []
    Y = []
    X.append(x_i)
    Y.append(y_i)
    while x_i < x_f:
        st_sz = min(st_sz, x_f - x_i)
        y_i += rk4(func, x_i, y_i, st_sz)
        x_i += st_sz
        X.append(x_i)
        Y.append(y_i)
    return np.array(X), np.array(Y)

def ex7_4():
    def F(x, y):
        F = np.zeros(2)
        F[0] = y[1]
        F[1] = -0.1*y[1] - x
        return F
    x0 = 0
    xf = 2
    y = np.array([0.0, 1.0])
    h = 0.2
    X, Y = runge_kutta4(F, x0, xf, y, h)
    plt.plot(X, Y)
    plt.show()

ex7_4()