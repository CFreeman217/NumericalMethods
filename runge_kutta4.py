import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(func, x_0, x_f, y_0, n=0, st_sz=0):
    '''
    Numerical Methods: Differential Equations, Initial Value Problems

    4th-order Runge-Kutta Method
    Does not include adaptive step size adjustment

    ** Requires numpy to return the np.array datatype and to handle the input vector in both func and y_0 **

    Input:
    func : Function to evaluate in the form F(x,y)
    x_0 : Initial value for x to start evaluating the integral
    x_f : Final value for x
    y_0 : Initial value for y when x = x_0
    n : Number of slices to use on the domain for the evaluation

    Output
    x : x-vector
    y : y-vector
    '''
    # Workhorse of the method - generates a weighted average for the slope estimate between the two points being evaluated
    def rk4(func, x_i, y_i, st_sz):
        k0 = st_sz*func(x_i, y_i)
        k1 = st_sz*func(x_i + st_sz/2.0, y_i + k0/2.0)
        k2 = st_sz*func(x_i + st_sz/2.0, y_i + k1/2.0)
        k3 = st_sz*func(x_i + st_sz, y_i + k2)
        return (k0 + 2.0*k1 + 2.0*k2 + k3)/6.0
    # Check for input on step size or number of segments
    if st_sz == 0 and n == 0:
        print('Error in Numeric Integration using RK4 method: Last argument must be either a step size or number of segments.\nUsage: X, Y = runge_kutta4(func, x_0, x_f, y_0, n=< # steps > ~OR~ st_sz=< step size >')
    # Generate a step size if number of segments is provided
    elif st_sz == 0:
        st_sz = (x_f - x_0) / n
    # Set up the initial values
    x_n = x_0
    y_n = y_0
    # Instantiate variables to hold the solutions
    X = []
    Y = []
    # Begin adding the intiial values to the solution vectors
    X.append(x_n)
    Y.append(y_n)
    # Generate the soltuion vector for the rest of the points
    while x_n < x_f:
        # Doing this handles the situation where not a big enough step size is provided
        st_sz = min(st_sz, x_f - x_n)
        y_n = y_n + rk4(func, x_n, y_n, st_sz)
        x_n = x_n + st_sz
        X.append(x_n)
        Y.append(y_n)
    # Set the solution in an array for easier numpy dumpy
    return np.array(X), np.array(Y)

def ex7_4():
    def fcn(x, y):
        fcn = np.zeros(2)
        fcn[0] = y[1]
        fcn[1] = -0.1*y[1] - x
        return fcn
    x0 = 0
    xf = 2
    y = np.array([0.0, 1.0])
    h = 0.2
    X, Y = runge_kutta4(fcn, x0, xf, y, n=0, st_sz=h)
    yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)
    plt.scatter(X,Y[:,0],label='RK4 Method')
    plt.plot(X,yExact,label='Exact Solution')
    plt.xlabel('X-Values')
    plt.ylabel('Y-Values')
    plt.title('4th-Order Runge-Kutta Example')
    plt.legend()
    plt.show()

ex7_4()