def mat_pivot(in_matrix):
    '''
    Pivots the input matrix to put the largest value on the diagonal. Returns an identity
    matrix that needs to be multiplied into the original matrix to yield the original
    transformed matrix
    '''
    n_row = len(in_matrix)

    # Generates an identity matrix using the result of the boolean test that runs down the
    # column and row for the matrix size.
    identity_mat = [[float(i==j) for i in range(n_row)] for j in range(n_row)]

    for item in range(n_row):
        # Rearrange the identity matrix so that the largest absolute value for each element
        # is on the diagonal
        row = max(range(item, n_row), key=lambda i: abs(in_matrix[i][item]))
        if item != row:
            # Swap the rows
            identity_mat[item], identity_mat[row] = identity_mat[row], identity_mat[item]

    return identity_mat