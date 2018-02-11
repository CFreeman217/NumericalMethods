def example2():
    c_matrix = [[8,8],\
                [3,1]]
    e_elem = [-24,23]
    naive_gauss(c_matrix, e_elem)

def example():
    c_matrix = [[2,1,3],\
                [4,4,7],\
                [2,5,9]]
    e_elem = [1,1,3]
    naive_gauss(c_matrix, e_elem)

def naive_gauss(coef_matrix, known_array):
    '''
    Numerical Methods : Naive Gauss Elimination

    Solves a system of equations using matrix of coefficients and array of
    known_index values. This is a two step process: 
    1. ) Forward elimination yields an upper triangular matrix
    2. ) Back substitution solves the equations and assembles the solution
            matrix

    coef_matrix : Array of coefficients for the equations we are trying to solve
    known_array : Array of constants
    '''
    # FORWARD ELIMINATION - 
    # The goal here is to get an upper triangular
    # Get the size of the array
    array_size = len(coef_matrix)
    # Output list to hold solution values
    output_list = []
    # Using list indices, the pivot row is row zero for the first iteration
    # and goes up to the next to last row
    for pivot_row in range(array_size - 1):
        # The elimination row is the row after the pivot row. The range function
        # is zero indexing by default
        for elim_row in range(pivot_row + 1, array_size):
            # The multiplication factor is generated by finding a number that cancels out
            # the far left term in the elimination row.
            multi_fac = coef_matrix[elim_row][pivot_row]/coef_matrix[pivot_row][pivot_row]
            # Now we need to go value by value across the coefficient array (horizontally)
            for column in range(array_size):
                # Set the new coefficient values for the elimination row by subtracting the
                # elimination row coefficient value from the product of the multiplication factor and 
                # the pivot row coefficient
                coef_matrix[elim_row][column] -= multi_fac * coef_matrix[pivot_row][column]
            # Set the new values for the known_index array using the same method as the coefficient
            # matrix values
            known_array[elim_row] -= multi_fac * known_array[pivot_row]

    # At this point, both the coefficient matrix and the known value array have been transformed
    # into an upper triangular matrix that can be used to solve for the unknown values

    # BACK SUBSTITUTION - Solve the system of equations from bottom to top

    # Use iterations of 'row' to determine the distance from the bottom of the matrix to find
    # solutions for
    for calc_row in range(-1,-(array_size+1),-1):
        # Initiate a value to hold the sum of the known variables and coefficients
        total = 0
        # Iterations of 'found_value' begin at -1 and stop when equal to the row we are calculating
        for found_value in range(-1,row,-1):
            # For each value that has been found so far, multiply the coefficient matrix
            # values for this row by the found values
            total += output_list[known_index]*coef_matrix[row][known_index]
        # Subtract the sum of the known quantities from the given input array for the row we are calculating
        # Divide all of this by the coefficient of the unknown variable to find the value for the unknown.
        # Do some fancy maneuvering to append this to the top of the output list, building the solution
        # from the bottom up.
        output_list = [(known_array[calc_row] - total) / coef_matrix[calc_row][calc_row]] + output_list
    print(output_list)
    return(output_list)
example()
example2()