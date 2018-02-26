
def mat_mult(mat_m, mat_n):
    '''
    Multiplies two matrices m and n_size
    '''
    # Generate a matrix of zeros to hold the output
    result = [[0] * len(mat_m) for z_col in range(len(mat_n[0]))]
    # Iterate across rows
    for row in range(len(mat_m)):
        # Then go by column
        for col in range(len(mat_n[0])):
            # Then select each value from the matrices
            for val in range(len(mat_n)):
                # Change the value in the zero matrix
                result[row][col] += mat_m[row][val] * mat_n[val][col]
    return result

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

def lu_decomp(input_matrix):
    '''
    Yields the lower and upper decomposition for the input matrix (must be square)
    Returns :

    lower : Lower triangular matrix
    upper : Upper triangular matrix
    '''
    n_size = len(input_matrix)

    # Generate zero matrices for lower and upper
    lower = [[0] * n_size for i in range(n_size)]
    upper = [[0] * n_size for i in range(n_size)]

    # Create pivot matrix pivot and multiplied matrix new_mat
    pivot = mat_pivot(input_matrix)
    new_mat = mat_mult(pivot,input_matrix)

    # Perform LU Decomposition
    for j in range(n_size):
        # All diagonal numbers for lower are set to 1
        lower[j][j] = 1

        for i in range(j+1):
            sum_up = sum(upper[k][j] * lower[i][k] for k in range(i))
            upper[i][j] = new_mat[i][j] - sum_up

        for i in range(j, n_size):
            sum_low = sum(upper[k][j]* lower[i][k] for k in range(j))
            lower[i][j] = (new_mat[i][j] - sum_low) / upper[j][j]

    return lower, upper

A = [[3, -2, 1],
     [2, 6, -4],
     [-1, -2, 5]]


L, U = lu_decomp(A)

print('Input :')
for line in A:
    print(line)


print('Lower :')
for line in L:
    print(line)
print('Upper :')
for line in U:
    print(line)
