## module prob25_1
'''Problem 25_1 test case for euler's method'''
import matplotlib.pyplot as plt
from euler import euler

def prob25_1():
    # Input function
    in_fun = lambda t, y : y*(t**2) - 1.1*y
    # Initial values
    x1_0 = 0
    x1_f = 2
    y1_0 = 1
    n1_s = 4
    n2_s = 8
    # Run the function
    X1, Y1 = euler(in_fun, x1_0, x1_f, y1_0, n1_s)
    X2, Y2 = euler(in_fun, x1_0, x1_f, y1_0, n2_s)
    # plot
    plt.plot(X1, Y1, label='Euler h=0.5')
    plt.plot(X2, Y2, label='Euler h=0.25')
    plt.xlabel('X - Values')
    plt.ylabel('Y - Values')
    plt.title('Euler Method Step Size Comparison')
    plt.legend()
    plt.show()
prob25_1()