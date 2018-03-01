def main():
    '''
    Associated with Problem 6.9 b & c
    '''

    # Initial functions to find the root
    funct = lambda x : x**3 - 6*x**2 + 11*x - 6.1
    # Derivative of the first function for Newton-Rhapson
    funct_p = lambda x : 3*x**2 - 12*x + 11
    x_init = 3.5 # Initial guess
    x_i = 2.5 # Initial first guess for the i term in secant method
    er_lim = 0.005 # Error limit of less than 0.5%
    max_i = 3 # Max iterations
    newton_raphson(funct, funct_p, x_init, er_lim, max_i)
    nm_secant(funct, x_init, x_i, er_lim, max_i)


def newton_raphson(funct, fderiv, initial_guess, er_limit=0, max_iter=10):
    '''
    Numerical Methods - Roots of functions

    Newton-Raphson Method

    These open methods do not require both of the initial guesses to straddle
    the root, but sometimes these methods do not converge.
    Newton-Raphson is one of the more widely used algorithms.

    These methods converge at least twice as fast as bracketing methods
    

    funct : The function you are finding the root for
    fderiv : The first derivative of funct
    initial_guess : Starting point for calculation
    er_limit : Estimated Error Threshold (Optional)
    max_iter : Maximum iterations (Optonal, default is 10)
    
    '''
    x_guess = initial_guess
    for iter_no in range(max_iter):
        old_guess = x_guess
        y_guess = funct(x_guess)
        dy_guess = fderiv(x_guess)
        x_guess = x_guess - y_guess / dy_guess
        # Calculate the current estimated error on this iteration
        c_error = abs((x_guess - old_guess) / x_guess)
        if c_error < er_limit:
            # The calculated error has dropped below the required threshold
            break
    print('\nNewton-Raphson Method Results : \n')
    print('Approximated Value : {}'.format(x_guess))
    print('Function Output : {}'.format(y_guess))
    print('Estimated Error : {}'.format(c_error))
    print('Iteration Count : {}'.format(iter_no + 1))

def nm_secant(funct, xi_1 , xi, er_limit=0, max_iter=100):
    '''
    Numerical Methods - Roots of functions

    Secant Method

    These open methods do not require both of the initial guesses to straddle
    the root, but sometimes these methods do not converge.
    

    funct : The function you are finding the root for
    xi_1 : The i+1 term of the x starting values
    xi : The i-th term of starting values
    er_limit : Estimated Error Threshold (Optional)
    max_iter : Maximum iterations (Optional, default is 10)
    
    '''
    # Gather information on the function at the starting points
    x_plus1 = xi_1
    y_plus1 = funct(x_plus1)
    x_guess = xi
    y_guess = funct(x_guess)
    # Iterate within the loop parameters
    for iter_no in range(max_iter):
        # Store the previous values
        x_plus2 = x_plus1
        y_plus2 = y_plus1
        x_plus1 = x_guess
        y_plus1 = y_guess
        # Generate a new guess and output
        x_guess = x_plus1 - (y_plus1 * (x_plus2 - x_plus1))/(y_plus2 - y_plus1)
        y_guess = funct(x_guess)
        # Calculate the current estimated error on this iteration
        c_error = abs((x_guess - x_plus1) / x_guess)
        if c_error < er_limit:
            # The calculated error has dropped below the required threshold
            break
    print('\nSecant Method Results : \n')
    print('Approximated Value : {}'.format(x_guess))
    print('Function Output : {}'.format(y_guess))
    print('Estimated Error : {}'.format(c_error))
    print('Iteration Count : {}'.format(iter_no + 1))

main()
