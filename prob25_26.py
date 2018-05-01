## module prob25_26
'''
Demonstration of adaptive RK4/5 method on a system of 2nd order differential equations
'''
import numpy as np
import matplotlib.pyplot as plt
from runge_kutta5 import runge_kutta5

def prob25_26():
    def fcn(t, x):
        fcn = np.zeros(6)

        m1 = 60
        m2 = 70
        m3 = 80
        g = 9.81
        k1 = 50
        k2 = 100
        k3 = 50
        fcn[0] = x[3]
        fcn[1] = x[4]
        fcn[2] = x[5]
        fcn[3] = g + (k2/m1)*x[1] - ((k1 + k2)/m1)*x[0]
        fcn[4] = g + (k2/m2)*x[0] - ((k2 + k3)/m2)*x[1] + (k3/m2)*x[2]
        fcn[5] = g + (k3/m3)*x[1] - (k3/m3) * x[2]
        return fcn

    t0 = 0
    tf = 100
    x = np.array([0]*6)
    X, Y = runge_kutta5(fcn, t0, tf, x)

    plt.plot(X, Y[:,0], label='m1 = 60kg')
    plt.plot(X, Y[:,1], label='m2 = 70kg')
    plt.plot(X, Y[:,2], label='m3 = 80kg')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement')
    plt.title('Bungee Jumper Displacement')
    plt.legend()
    plt.show()

    plt.plot(X, Y[:,3], label='m1 = 60kg')
    plt.plot(X, Y[:,4], label='m2 = 70kg')
    plt.plot(X, Y[:,5], label='m3 = 80kg')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Bungee Jumper Velocity')
    plt.legend()
    plt.show()
prob25_26()