import numpy as np
import matplotlib.pyplot as plt

def cfdd_1deriv(fcn, val, step):
    '''
    Numerical Methods : Numeric Differentiation

    Centered Finite Divided Difference - 1st Derivative

    Calculates the derivative of a function numerically

    fcn : Function to evaluate
    val : Value to evaluate the function at
    step : Step size for generating the estimation

    Returns derivative
    '''
    # Get two steps away
    t_step = 2*step
    # Function minus 2 steps
    fx_m2 = fcn(val - t_step)
    # Function minus 1 step
    fx_m1 = fcn(val - step)
    # Function plus 1 step
    fx_p1 = fcn(val + step)
    # Function plus 2 steps
    fx_p2 = fcn(val + t_step)
    # Run through Taylor series approximation
    return ((-fx_p2 + 8*fx_p1 - 8*fx_m1 + fx_m2)/(12*step))

def num_1deriv(x_list, y_list, val):
    '''
    Numerical Methods - Numeric Differentiation of a list of data points
    returns first derivative
    Forward Finite Divided difference at the start, Backward at the end, and centered in the middle
    '''
    x_index = []
    x_val = 0
    y_val = 0
    for key, x_num in enumerate(x_list):
        if val > x_num:
            # Linear Interpolation of value from points
            x_index.append(key)
            x_val = val
            y_val = y_list[key-1] + val * ((y_list[key] - y_list[key-1]) / (x_num - x_list[key-1]))
            break
        elif val == x_num:
            x_index.append(key)
            x_val = x_num
            y_val = y_list[key]
            break
    if x_index == []:
        print('Input value not found in the dataset. Make sure that the differentiating point is within the bounds of the x_values')
        
        
    
            

    if val in x_list:
        return
    st_sz = abs(x_list[0] - x_list[1])
    out_list = []
    n_size = len(y_list)
    for i_x, value in enumerate(y_list):
        if i_x == 0:
            f_deriv = value
            # # First data point uses Forward Finite Divided Difference
            # p_2 = y_list[i_x+2]
            # p_1 = y_list[i_x+1]
            # f_deriv = (-p_2 + 4*p_1 - 3*value)/(2*st_sz)

        if i_x == 1 or i_x == n_size-2:
            # The end points do not have as much data so the derivative loses accuracy, fewer series terms available
            p_1 = y_list[i_x+1]
            m_1 = y_list[i_x-1]
            f_deriv = ((p_1) - (m_1))/(2*st_sz)

        elif i_x > 1 and i_x < n_size-2:
            # Centered method while the data exists
            p_2 = y_list[i_x+2]
            p_1 = y_list[i_x+1]
            m_1 = y_list[i_x-1]
            m_2 = y_list[i_x-2]
            f_deriv = (-p_2 + 8*p_1 - 8*m_1 + m_2)/(12*st_sz)

        elif i_x == n_size -1:
            # # Last data point uses Backward Finite Divided Difference
            # m_2 = y_list[i_x-2]
            # m_1 = y_list[i_x-1]
            # f_deriv = (m_2 - 4*m_1 + 3*value)/(2*st_sz)
            f_deriv = value


        out_list.append(f_deriv)
    return out_list

def num_2deriv(x_list, y_list):
    '''
    Numerical Methods - Numeric Differentiation of a list of data points
    returns second derivative
    Forward Finite Divided difference at the start, Backward at the end, and centered in the middle
    '''
    st_sz = abs(x_list[0] - x_list[1])
    out_list = []
    n_size = len(y_list)
    for i_x, value in enumerate(y_list):
        if i_x == 0:
            # First data point uses Forward Finite Divided Difference
            p_3 = y_list[i_x+3]
            p_2 = y_list[i_x+2]
            p_1 = y_list[i_x+1]
            f_deriv = (-p_3 + 4*p_2 - 5*p_1 + 2*value)/(st_sz**2)

        if i_x == 1 or i_x == n_size-2:
            # The end points do not have as much data so the derivative loses accuracy, fewer series terms available
            p_1 = y_list[i_x+1]
            m_1 = y_list[i_x-1]
            f_deriv = (p_1 - 2*value + m_1)/(st_sz**2)

        elif i_x > 2 and i_x < n_size-2:
            # Centered method while the data exists
            p_2 = y_list[i_x+2]
            p_1 = y_list[i_x+1]
            m_1 = y_list[i_x-1]
            m_2 = y_list[i_x-2]
            f_deriv = (-p_2 + 16*p_1 - 30*value + 16*m_1 - m_2)/(12*st_sz**2)

        elif i_x == n_size -1:
            # Last data point uses Backward Finite Divided Difference
            m_3 = y_list[i_x-3]
            m_2 = y_list[i_x-2]
            m_1 = y_list[i_x-1]
            f_deriv = (2*value - 5*m_1 + 4*m_2 - m_3)/(st_sz**2)
            
        out_list.append(f_deriv)
    return out_list

def test_num():

    x_data = np.linspace(0, 1, 100)
    y_data = lambda x : x**2
    d_data = num_1deriv(x_data, y_data(x_data))
    # plt.plot(x_data, y_data(x_data), label='Function')
    # plt.plot(x_data, d_data, label='Derivative')
    # plt.legend()
    # plt.show()
def ex4_4():
    '''
    Test case for cfdd_1deriv
    '''
    func = lambda x : -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.25
    val = 0.5
    hgt = 0.5
    print(cfdd_1deriv(func, val, hgt))
    print(num_1deriv(x_list, y_list, val))
# test_num()
ex4_4()