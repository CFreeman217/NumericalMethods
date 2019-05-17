#! /usr/bin/env python3
## module ode45py
'''
Numerical Methods - Moderately stiff numeric ODE solvers

4th order - 5th order Runge-Kutta algorithm with adaptive step size
Uses Dormand-Prince coefficient matrix for adjusting weighting on the algorithm
This solver mimics MATLAB's ODE45 function.

ode45py(func, x, y, st_sz=1.0e-4, tol=1.0e-5)

    Input:
    func : Function to evaluate in the form F(x,y)
    x : x-vector containing initial and final values to evaluate the integral
    y : y-vector with functions to evaluate
    st_sz : Step size to run across the integral for initial estimate
    tol : Error estimate tolerance for determining whether to adjust step size

    Output:
    X : x-vector as numpy array
    Y : y-vector as numpy array

    See example_ode45py.py
'''
import numpy as np

def ode45py(func, x, y, st_sz=1.0e-4, tol=1.0e-6, iter_lim=50000):
    '''
    Numerical Methods: Differential Equations, Initial Value Problems

    4th-order / 5th-order Runge-Kutta Method
    Includes adaptive step size adjustment
    Imitates MATLAB ode45 functionality and output
    '''
    # Dormand-Prince coefficients for RK algorithm -
    a0 = 0; a1 = 0.2; a2 = 0.3; a3 = 0.8; a4 = 8/9; a5 = 1.0; a6 = 1.0
    c0 = 35/384; c1 = 0; c2 = 500/1113; c3 = 125/192; c4 = -2187/6784; c5=11/84; c6 = 0
    d0 = 5179/57600; d1 = 0; d2 = 7571/16695; d3 = 393/640; d4 = -92097/339200; d5 = 187/2100; d6 = 1/40
    b10 = 0.2
    b20 = 0.075; b21 = 0.225
    b30 = 44/45; b31 = -56/15; b32 = 32/9
    b40 = 19372/6561; b41 = -25360/2187; b42 = 64448/6561; b43 = -212/729
    b50 = 9017/3168; b51 = -355/33; b52 = 46732/5247; b53 = 49/176; b54 = -5103/18656
    b60 = 35/384; b61 = 0; b62 = 500/1113; b63 = 125/192; b64 = -2187/6784; b65 = 11/84

    # Cash-Karp coefficients for RK algorithm -
    # a0 = 0; a1 = 0; a2 = 1/5; a3 = 3/10; a4 = 3/5; a5 = 1.0; a6 = 7/8
    # c0 = 37/378; c1 = 0; c2 = 250/621; c3 = 125/594; c4 = 0; c5=512/1771; c6 = 0
    # d0 = 2825/27648; d1 =0; d2 = 18575/48384; d3 = 13525/55296; d4 = 277/14336; d5 = 1/4; d6 = 0
    # b10 = 0
    # b20 = 1/5; b21 = 0
    # b30 = 3/40; b31 = 9/40; b32 = 0
    # b40 = 3/10; b41 = -9/10; b42 = 6/5; b43 = 0
    # b50 = -11/54; b51 = 5/2; b52 = -70/27; b53 = 35/27; b54 = 0
    # b60 = 1631/55296; b61 = 175/512; b62 = 575/13824; b63 = 44275/110592; b64 = 253/4096; b65 = 0

    # Fehlberg coefficients for RK algorithm -
    # a0 = 0; a1 = 0; a2 = 1/4; a3 = 3/8; a4 = 12/13; a5 = 1.0; a6 = 1/2
    # c0 = 16/135; c1 = 0; c2 = 6656/12825; c3 = 28561/56430; c4 = -9/50; c5=2/55; c6 = 0
    # d0 = 25/216; d1 =0; d2 = 1408/2565; d3 = 2197/4104; d4 = -1/5; d5 = 0; d6 = 0
    # b10 = 0
    # b20 = 1/4; b21 = 0
    # b30 = 3/32; b31 = 9/32; b32 = 0
    # b40 = 1932/2197; b41 = -7200/2197; b42 = 7296/2197; b43 = 0
    # b50 = 439/216; b51 = -8; b52 = 3680/513; b53 = -845/4104; b54 = 0
    # b60 = -8/27; b61 = 2; b62 = -3544/2565; b63 = 1859/4104; b64 = -11/40; b65 = 0

    # Store initial values
    x_f = x[-1]
    x_n = x[0]
    # y_n = y
    # Initialize variables
    X = []
    Y = []
    # Add the first set of known conditions
    X.append(x_n)
    Y.append(y)
    # Set up to break the for loop at the end
    stopper = 0 # Integration stopper, 0 = off, 1 = on
    # Initialize a k0 to start with the step size
    # k0 = st_sz * func(x_n, y)
    # Generate the RK coefficients
    for i in range(iter_lim):
        k0 = st_sz * func(x_n + a0*st_sz, y)
        k1 = st_sz * func(x_n + a1*st_sz, y + b10*k0)
        k2 = st_sz * func(x_n + a2*st_sz, y + b20*k0 + b21*k1)
        k3 = st_sz * func(x_n + a3*st_sz, y + b30*k0 + b31*k1 + b32*k2)
        k4 = st_sz * func(x_n + a4*st_sz, y + b40*k0 + b41*k1 + b42*k2 + b43*k3)
        k5 = st_sz * func(x_n + a5*st_sz, y + b50*k0 + b51*k1 + b52*k2 + b53*k3 + b54*k4)
        k6 = st_sz * func(x_n + a6*st_sz, y + b60*k0 + b61*k1 + b62*k2 + b63*k3 + b64*k4 + b65*k5)
        # Getting to the slope is the whole point of this mess
        dy = c0*k0 + c1*k1 + c2*k2 + c3*k3 + c4*k4 + c5*k5 + c6*k6
        # Determine the estimated change in slope by comparing the output coefficients for each RK coefficient
        E = (c0 - d0)*k0 + (c1 - d1)*k1 + (c2 - d2)*k2 + (c3 - d3)*k3 + (c4 - d4)*k4 + (c5 - d5)*k5 + (c6 - d6)*k6
        # Find the estimated error using a sum of squares method
        e = np.sqrt(np.sum(E**2)/len(y))
        # we don't know if the new value i
        hNext = 0.9*st_sz*(tol/e)**0.2
        pcnt = (i/iter_lim)*100
        psolv = (x_n/x_f)*100
        print('Correction limit : {:1.2f}  x-domain solved: {:1.2f}'.format(pcnt, psolv))
        # If approximated error is within tolerance, accept this integration step and move on
        if e <= tol:
            # Store the new result
            i = i-1
            y = y + dy
            # Increment the x-value by the new step size
            x_n = x_n + st_sz
            # Add the new values into the output vector
            X.append(x_n)
            Y.append(y)
            # Check to break the loop when we have reached the desired x-value
            if stopper == 1: break # Reached end of x-range
            # Set limits on how much the next step size can increase to avoid missing data points
            if abs(hNext) > 10*abs(st_sz): hNext = 10*st_sz
            # Determine if the algorithm has reached the end of the dataset
            if (st_sz > 0.0) == ((x_n + hNext) >= x_f):
                hNext = x_f - x_n
                # Sets the break condition for the next loop iteration
                stopper = 1
                print('Success! Reached the end of the data set.')
            # Setting k0 to k6 * (next step size) / (current step size) forces the algorithm to use the 4th order formula for the next step
            k0 = k6*hNext/st_sz

        else:
            # The error estimate is outside the required threshold to move on, we need to redo the calculation with a smaller step size
            if abs(hNext) < abs(st_sz)*0.1 : hNext = st_sz*0.1
            # Set up k0 to go through the 5th order RK method on the next iteration because the error was no good.
            k0 = k0*hNext/st_sz
        # Set the next iteration step size
        st_sz = hNext

    # Returns the arrays for x and y values
    return np.array(X), np.array(Y)

