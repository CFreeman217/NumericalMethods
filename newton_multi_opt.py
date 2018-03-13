def newton_optimize(funct, fderiv, f2deriv, initial_guess, er_limit=0, max_iter=10):
    '''
    Numerical Methods - Newton Raphson Optimization

    Newton-Raphson Method

    These open methods do not require both of the initial guesses to straddle
    the root, but sometimes these methods do not converge.
    Newton-Raphson is one of the more widely used algorithms.

    These methods converge at least twice as fast as bracketing methods
    

    funct : The function you are finding the root for
    fderiv : The first derivative of funct
    f2deriv : The second derivative of funct
    initial_guess : Starting point for calculation
    er_limit : Estimated Error Threshold (Optional)
    max_iter : Maximum iterations (Optonal, default is 10)
    
    '''
    x_guess = initial_guess
    for iter_no in range(max_iter):
        old_guess = x_guess
        y_guess = fderiv(x_guess)
        dy_guess = f2deriv(x_guess)
        x_guess = x_guess - y_guess / dy_guess
        # Calculate the current estimated error on this iteration
        c_error = abs((x_guess - old_guess) / x_guess)
        if c_error < er_limit:
            # The calculated error has dropped below the required threshold
            print('Error threshold met within {} iterations.'.format(iter_no))
            break
    print('\nNewton-Raphson Optimization Results : \n')
    print('Approximated Value : {}'.format(x_guess))
    print('Function Output : {}'.format(funct(x_guess)))
    print('Estimated Error : {}'.format(c_error))
    print('Iteration Count : {}'.format(iter_no + 1))

def takehome_quiz():
    
    revenue = lambda x, y : 15*(x + y)
    cost1 = lambda x : 0.02*x**2 + 4*x + 500
    cost2 = lambda y : 0.05*y**2 + 4*y + 275
    total_cost = lambda x, y : cost1(x) + cost2(y)
    profit = lambda x, y : revenue(x, y) - total_cost(x, y)
    dPdx = 275
    dPdy = 110
    print(profit(dPdx, dPdy))
takehome_quiz()