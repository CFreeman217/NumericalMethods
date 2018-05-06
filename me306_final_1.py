from numpy import exp
import numpy as np
import matplotlib.pyplot as plt
from NumericalMethods import ode45py
import math as math

def me306_final_1():
    # d2T/dx2 - 0.15T = 0
    def func(x, T):
        parray = np.zeros(2)
        parray[0] = T[1]
        parray[1] = 0.15*T[0]
        return parray

    def analytical(in_val):
        epow = 10 * (0.15)**(0.5)
        lside = 150 - 240*exp(epow)
        c_2 = lside / (exp(-epow) - exp(epow))
        c_1 = 240 - c_2
        return (c_1 * exp(in_val*(0.15**0.5)) + c_2 * exp(-in_val*(0.15**0.5)))
    X1 = np.arange(0, 2, 0.01)
    Y1 = np.array([analytical(i) for i in range(len(X1))])
    x_startstop = [0,10]
    needed_val = 150
    guess1 = np.array([240, -95])
    guess2 = np.array([240, -90])
    h = 1
    Xa, Ya = ode45py(func, x_startstop, guess1, st_sz=h)
    Xb, Yb = ode45py(func, x_startstop, guess2 , st_sz=h)
    output1 = Ya[:,0][-1]
    output2 = Yb[:,0][-1]
    shoot_dx0 = [240,lininterp(needed_val, output1, output2, guess1[-1], guess2[-1])]
    X2, Y2 = ode45py(func, x_startstop, shoot_dx0 , st_sz=h)
    plt.plot(X1, Y1, label='Analytical Solution')
    plt.plot(X2, Y2[:,0], ':', label='Shooting Method Result')
    plt.plot(Xa, Ya[:,0], label='Guess 1')
    plt.plot(Xb, Yb[:,0], label='Guess 2')
    plt.xlabel('X - Values')
    plt.ylabel('Y - Values')
    plt.title('Boundary Problem Solution Methods')
    plt.legend()
    plt.savefig('ME399_prob_1b.png',bbox_inches='tight')
    plt.show()

def lininterp(p_in, p1, p2, q1, q2):
    q_out = (q1 * (p2 - p_in) + q2 * (p_in - p1)) / (p2 - p1)
    return q_out

me306_final_1()
