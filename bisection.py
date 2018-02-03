
def main():
    '''
    Problem 5-16b : Critical Depth of Trapezoidal Channel
    '''
    Q = 20 # m^3/s - Flow Rate
    g = 9.81 # m/s^2 - Gravity
    # Function to iterate over
    f = lambda x : 1 - (Q**2 / (g * (3*x + x**2/2)**3))*(3 + x)
    low = 0.5 # Lower Guess
    high = 2.5 # Upper Guess
    er = 0.01 # Boundary Limit
    m_it = 10 # Maximum Iterations
    # Call the bisection subroutine
    bisection(f,low,high,er,m_it)


def bisection(funct, lowerguess, upperguess, er_limit, max_iter):
    '''
    Numerical Methods - Bisection Method:

    Select two x-values that yield function outputs of opposite sign and
    this function performs bisection to find the root.

    funct : Function to evaluate the root
    lowerguess : Initial lower guess for x
    upperguess : Initial upper guess for x
    er_limit : Desired approximate error
    max_iter : Maximum number of iterations allowed
    '''
    # Find the point information from the function
    x_lower = lowerguess
    y_lower = funct(lowerguess)
    x_upper = upperguess
    y_upper = funct(upperguess)
    # Current error is set at 100%
    c_error = 1.0
    # Initialize current guess
    x_guess = 0
    # Initialize iteration counter
    i_count = 0
    # While current error is outside the desired estimate and we are
    # within the iteration limit
    while c_error > er_limit and i_count < max_iter:
        # Cycle the iterator
        i_count += 1
        # Store the previous value
        old_guess = x_guess
        # Generate a new guess for an x-value
        x_guess = (x_lower + x_upper) / 2
        # Create the corresponding y-value from the input function
        y_guess = funct(x_guess)
        # If the output from the guess and the lower bound are on the
        # same side of the x-axis.
        if y_guess * y_lower > 0:
            # The lower bound needs to be adjusted to the new guess
            x_lower = x_guess
            y_lower = y_guess
        elif y_guess * y_upper > 0:
            # Otherwise the other boundary needs to be adjusted
            x_upper = x_guess
            y_upper = y_guess
        else:
            # A true zero has been found
            break
        c_error = abs((x_guess - old_guess) / x_guess)
    print('\nFinding root by bisection method : ')
    print('Approximate Root after {} operations is : {}'.format(i_count, x_guess,))
    print('Estimated Error : {}'.format(c_error))
    return x_guess, y_guess

main()
