def main():
    '''
    Numerical Methods - Roots of functions

    Newton-Raphson and Secant Methods

    These open methods do not require both of the initial guesses to straddle
    the root, but sometimes these methods do not converge.
    Newton-Raphson is one of the more widely used algorithms.

    Associated with Problem 6.9 b & c
    '''

    # Initial functions to find the root
    funct = lambda x : x**3 - 6*x**2 + 11*x - 6.1
    # Derivative of the first function
    funct_p = lambda x : 3*x**2 - 12*x + 11

    # Newton - Raphson Method
    x_init = 3.5 # Initial guess
    y_init = funct(x_init) # Initial output
    er_lim = 0.005 # Error limit of less than 0.5%
    c_error = 1 # Current guess error
    # Initialize iteration counter
    i_count = 0
    # Initialize the root guess
    x_guess = x_init
    y_guess = y_init
    # Find derivative output value
    y_slope = funct_p(x_guess)
    # While we are outside the error threshold and under our iteration count
    while c_error > er_lim and i_count < 3:
        # Cycle the iterator
        i_count += 1
        # Store prevous iteration information
        old_guess_x = x_guess
        old_guess_y = y_guess
        old_slope_y = y_slope
        # Guess a new root location and store the new outputs
        x_guess = old_guess_x - old_guess_y / old_slope_y
        y_guess = funct(x_guess)
        y_slope = funct_p(x_guess)
        # Calculate estimated error
        c_error = abs((x_guess - old_guess_x) / x_guess)
    print('From Newton-Raphson Method :')
    print('Approximate Root after {} operations is : {}'.format(i_count, x_guess))
    print('Estimated Error : {}'.format(c_error))
    
    # Secant Method
    x_init_1 = 3.5 # Initial first guess for the i+1 term
    y_init_1 = funct(x_init_1) # Initial output for the i+1 term
    x_init = 2.5 # Initial first guess for the i term
    y_init = funct(x_init) # Initial output for the i term
    er_lim = 0.005 # Error limit of less than 0.5%
    c_error = 1 # Current guess error
    # Initialize iteration counter
    i_count = 0
    # While we are outside the error threshold and under our iteration count
    while c_error > er_lim and i_count < 3:
        # Cycle the iterator
        i_count += 1
        # Update previous values
        x_i_2 = x_init_1 # The i+2 term for the x-guess
        y_i_2 = y_init_1 # Corresponding output
        x_init_1 = x_init # Sequence variables up the chain
        y_init_1 = y_init # Same for output
        # Secant method
        x_init = x_init_1 - (y_init_1 * (x_i_2 - x_init_1))/(y_i_2 - y_init_1)
        # Store the new function output
        y_init = funct(x_init)
        # Calculate the current Error for this iteration
        c_error = abs((x_init - x_init_1) / x_init)
    print('\nFrom Secant Method :')
    print('Approximate Root after {} operations is : {}'.format(i_count, x_init))
    print('Estimated Error : {}'.format(c_error))
        
main()
