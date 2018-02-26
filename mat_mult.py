
def mat_mult(mat_m, mat_n):
    '''
    Multiplies two matrices m and n
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



a = [[34,1,77],
     [2,14,8],
     [3,17,11]]
b = [[6,8,1],
     [9,27,5],
     [2,43,31]]

c = [[1,2,3],
     [4,5,6]]

d = [[7,8],
     [9,10],
     [11,12]]

e = [[1,6],
     [3,10],
     [7,4]]

f = [[1,3],
     [.5,2]]
print(mat_mult(c,d))


