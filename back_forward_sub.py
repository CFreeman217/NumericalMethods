def back_sub(input_matrix, known_values):
    '''
    Performs back substitution on a given input matrix with a vector of known values.
    Returns the results for the coefficients
    '''
    # Get the size of the coefficient matrix and make sure it is square
    a_rows = len(input_matrix)
    a_cols = len(input_matrix[0])
    if a_rows != a_cols:
        print('Input matrix must be square')
        exit
    results = []
    # Use iterations of 'calc_row' to determine the distance from the bottom of the matrix to find
    # solutions for the values starting from the last row and ending once the first row has been calculated
    for calc_row in range(-1,-(a_rows+1),-1):
        # Initiate a value to hold the sum of the known variables and coefficients
        total = 0
        # Iterations of 'found_value' begin at -1 and stop when equal to the row we are calculating.
        # this loop is not entered for the first iteration because calc_row begins at -1
        for found_value in range(-1,calc_row,-1):
            # For each value that has been found so far, multiply the coefficient matrix
            # values for this row by the found values and sum them.
            total += results[found_value]*input_matrix[calc_row][found_value]
        # Subtract the sum of the known quantities from the given input array for the row we are calculating
        # Divide all of this by the coefficient of the unknown variable to find the value for the unknown.
        # Do some fancy maneuvering to append this to the top of the output list, building the solution
        # from the bottom up.
        results = [(known_values[calc_row] - total) / input_matrix[calc_row][calc_row]] + results
    return results

def forward_sub(input_matrix, known_values):
    '''
    Performs forward substitution on a given input coefficient matrix and a vector matrix of known values.
    Returns a results vector matrix that can be sent into the back substitution method.
    '''
    # Get the size of the coefficient matrix and make sure it is square
    a_rows = len(input_matrix)
    a_cols = len(input_matrix[0])
    if a_rows != a_cols:
        print('Input matrix must be square')
        exit
    results = [known_values[0]]
    # Use iterations of 'calc_row' to determine the distance from the bottom of the matrix to find
    # solutions for the values starting from the last row and ending once the first row has been calculated
    for calc_row in range(1,a_rows):
        # Initiate a value to hold the sum of the known variables and coefficients
        total = 0
        # Iterations of 'found_value' begin at -1 and stop when equal to the row we are calculating.
        # this loop is not entered for the first iteration because calc_row begins at -1
        for found_value in range(calc_row):
            # For each value that has been found so far, multiply the coefficient matrix
            # values for this row by the found values and sum them.
            total += results[found_value]*input_matrix[calc_row][found_value]
        # Subtract the sum of the known quantities from the given input array for the row we are calculating
        # Divide all of this by the coefficient of the unknown variable to find the value for the unknown.
        # Do some fancy maneuvering to append this to the top of the output list, building the solution
        # from the bottom up.
        results += [(known_values[calc_row] - total) / input_matrix[calc_row][calc_row]]
    return results