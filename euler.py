import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

def prob25_1():
    in_fun = lambda t, y : y*(t**2) - 1.1*y
    x1_0 = 0
    x1_f = 2
    y1_0 = 1
    n1_s = 4
    n2_s = 8
    X1, Y1 = euler(in_fun, x1_0, x1_f, y1_0, n1_s)
    X2, Y2 = euler(in_fun, x1_0, x1_f, y1_0, n2_s)
    plt.plot(X1, Y1, label='Euler h=0.5')
    plt.plot(X2, Y2, label='Euler h=0.25')
    plt.show()

def online():
    x0 = 0
    y0 = 1
    xf = 10
    n = 100
    in_fun = lambda x,y : -y + np.sin(x)
    X, Y = euler(in_fun, x0, xf, y0, n)
    plt.plot(X, Y)
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Approximate Solution with Forward Euler\'s Method')
    plt.show()

def euler(func, x_0, x_f, y_0, n):
    '''
    Numerical Methods - Differential Equation Initial Value Problems

    ** Requires NUMPY import **
    import numpy as np

    Euler Method:

    Inputs:
    func : function with variables in the form of f(x,y)
    x_0, x_f : beginning and end points to evaluate the integral
    y_0 : Initial value for the dependent variable(s). Feed a 2-D numpy array to solve multiple equations.
    n : Number of intervals to use between x_0, x_f

    Outputs:
    x : List of independent variable values
    y : List of dependent variable values for each equation
    '''
    # Determine the step size
    d_x = (x_f - x_0) / (n)
    # Create a vector of x-values
    x = np.linspace(x_0, x_f, n+1)
    # Generate a vector to hold y-values
    y = np.zeros([n+1])
    # Set the first initial value
    y[0] = y_0
    # Iterate through the calculation
    for i in range(1,n+1):
        # The next point is found by evaluating the function at this point
        y[i] = d_x*(func(x[i-1],y[i-1])) + y[i-1]
    # Return x and y vectors
    return x, y





prob25_1()
# online()