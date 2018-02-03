''' https://github.com/CFreeman217/NumericalMethods.git '''

def main():
    '''
    Problem 5-17 : Estimating volume of spherical tank
    '''
    from math import pi
    R = 3 # meters - Radius of tank
    V = 30 # m^3 - Volume to estimate
    m_it = 3 # Iteration limit
    # Volume of sphere minus estimation volume (find zero for this function)
    f = lambda h : pi * h ** 2 * (3*R - h)/3 - V
    h_low = 0 # Lower guess
    h_high = R # Upper guess

    false_position(f, h_low, h_high, m_it)

def false_position(funct, lowerguess, upperguess, max_iter):
    '''
    Numerical Methods - Roots of functions
    
    False Position Method:

    Takes a function with lower and upper bounds to find the root
    after an iteration limit with error approximation using false
    position.

    funct : Function to evaluate the root
    lowerguess : Initial lower guess for x
    upperguess : Initial upper guess for x
    max_iter : Maximum number of iterations allowed
    '''
    # Find the point information from the function
    x_lower = lowerguess
    y_lower = funct(lowerguess)
    x_upper = upperguess
    y_upper = funct(upperguess)
    # Initialize a guess
    x_guess = 0
    # Initialize iteration counter
    i_count = 0
    # While within the iteration count
    while i_count < max_iter:
        # Cycle the iterator
        i_count += 1
        # Store the previous value
        old_guess = x_guess
        # Generate a new guess for the root
        x_guess = x_upper - (y_upper * (x_lower - x_upper))/(y_lower - y_upper)
        # Find the function output from the new guess
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
        # Calculate the current estimated error on this iteration
        c_error = abs((x_guess - old_guess) / x_guess)
    # Print output
    print('After {} iterations, the approximate root has been calculated...'.format(i_count))
    print('Approximate Value : {} \t Estimated Error : {}'.format(x_guess, c_error))

main()
