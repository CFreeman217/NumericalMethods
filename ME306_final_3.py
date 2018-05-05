import numpy as np 
import matplotlib.pyplot as plt
from NumericalMethods import ode45py

def me306_final_3():
    def func(time, theta):
        fcn = np.zeros(4)        
        l1 = 1
        l2 = 2
        m1 = 2
        m2 = 1
        g = 9.8
        a = (m1 + m2) * l1
        b = m2*l2*np.cos(theta[0] - theta[2])
        c = m2*l1*np.cos(theta[0] - theta[2])
        d = m2*l2
        e = -m2*l2*(theta[3]**2)*np.sin(theta[0] - theta[2]) - g*(m1 + m2)*np.sin(theta[0])
        f = m2*l1*(theta[1]**2)*np.sin(theta[0] - theta[2]) - m2*g*np.sin(theta[2])
        # d_theta1/dt = 
        fcn[3] = (f*a - c*e) / (d*a - b*c)
        fcn[2] = theta[2]
        fcn[1] = (e - b*fcn[3])/a 
        fcn[0] = theta[0]
    i_theta = np.array([0.1, 0.0, 0.17, 0.0])
    d_time = np.array([0,100])

    X, Y = ode45py(func, d_time, i_theta)

    plt.plot(X,Y)
    plt.show()
me306_final_3()