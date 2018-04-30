## module prob11_3.py
'''
Test case for thomas algorithm for solving tridiagonal systems of equations
'''
from thomas import thomas
def prob11_3():
    '''
    The following tridiagonal system must be solved as part of a larger algorithm
    (Crank-Nicholson) for solving partial differential equations. Use the Thomas
    algorithm to obtain a solution
    '''
    # The primary diagonal
    in_f = [2.01475] * 4
    # Bottom coefficients
    in_e = [-0.020875] * 3
    # Top coefficients
    in_g = in_e
    # known vector
    in_b = [4.175, 0, 0, 2.0875]
    ans = thomas(in_f, in_e, in_g, in_b)
    print(ans)
prob11_3()