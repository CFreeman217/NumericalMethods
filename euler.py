import numpy as np 
import matplotlib.pyplot as plt 
from numpy import ndarray

def prob25_1():
    in_fun = lambda t, y : y*np.power(t,2) - 1.1*y 
    step = 0.01
    time = np.array([i*step for i in range(int(2/step))])
    x1_0 = np.array([[0]])
    x1_f = np.array([[2]])
    y1_0 = np.array([[1]])
    n1_s = 4
    X1, Y1 = euler(in_fun, x1_0, x1_f, y1_0, n1_s)
    plt.plot(X1, Y1)
    plt.show()

def euler(func, x_0, x_f, y_0, N):
    '''
    Numerical Methods - Differential Equation Initial Value Problems
    
    ** Requires NUMPY import **
    import numpy as np

    Euler Method:

    Inputs:
    func : function with variables in the form of f(x,y)
    x_0, x_f : beginning and end points to evaluate the integral
    y_0 : Initial value for the dependent variable(s). Feed a 2-D numpy array to solve multiple equations.
    N : Number of intervals to use between x_0, x_f

    Outputs:
    X : List of independent variable values
    Y : List of dependent variable values for each equation
    '''
    if N < 2:
        N = 2
    h = (x_f - x_0) / N
    X = [None] * (N+1)
    numcols = y_0.shape[1]
    Y = [[None]*numcols]*(N+1)
    
    x_n = x_0
    X[0] = x_n
    y_n = y_0
    Y = y_n.conj().T
    print(Y)
    for i in range(N):
        k1 = h*func(x_n, y_n)
        y_n = y_n + k1
        x_n = x_n + h
        X[i+1] = x_n
        Y[i+1][0] = y_n.conj().T
        
    return X,Y

def euler2(func, x_0, x_f, y_0, N):
    if N < 2:
        N = 2
    h = (x_f - x_0)/N
    x_vec = []
    max_y = len(y_0)
    y_vec = [[]]
    x = x_0
    x_vec.append(x)
    y = y_0
    y_vec[0] = y.conj().T

    for i in range(N):
        k1 = h*feval(func, x)
def feval(funcName,*args):
    return eval(funcName)(*args)
prob25_1()
