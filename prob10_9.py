## module prob10_9
'''
Solve the system of equations using LU Decomposition and back substitution
'''
from matrix_mods import lu_decomp, forward_sub, back_sub
def prob10_9():
    '''
    Solve the system of equations using LU Decomposition and back substitution
    '''
    mat_A = [[ 3, -2, 1],
             [ 2,  6,-4],
             [-1, -2, 5]]
    vec_B = [-10,
              44,
             -26]
    lowr, upr = lu_decomp(mat_A)
    print('Lower Matrix : ')
    for line in lowr:
        print(line)
    print('Upper Matrix : ')
    for line in upr:
        print(line)
    res_D = forward_sub(lowr,vec_B)
    print('Forward Vector : ')
    for line in res_D:
        print(line)
    sol = back_sub(upr,res_D)
    print('Solution : ')
    for line in sol:
        print(line)
prob10_9()