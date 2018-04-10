import numpy as np

def sim_int(fcn, l_bnd, u_bnd, n_point=100):
    '''
    Numerical Methods - Closed Numerical Integration

    Simpson's Rules

    Numerically integrates a function within lower and upper bounds over
    a given number of data points using second and third order Lagrange
    polynomials to approximate the function

    fcn : Function to integrate
    l_bnd : Lower bound on integration
    u_bnd : Upper bound on integration
    n_point : Number of data points to consider (default is 100)

    returns sum of the area below the curve of the function
    '''
    # Trapezoidal area
    trap = lambda h, f_0, f_1 : h * (f_0 - f_1) / 2
    def simp_38(h, f_0, f_1, f_2, f_3):
        '''
        Simpson's 3/8ths rule: Approximates a 3rd order Lagrange
        polynomial fit to four points.
        '''
        return (3*h * (f_0 + 3* (f_1 + f_2) + f_3) / 8)
    def simp_13m(fcn, h, n):
        '''
        Simpson's 1/3rd rule: Multiple Application: Feed a function,
        height and number of points. Needs odd number of points
        '''
        simp13_sum = fcn(0)
        for i in range(1, n-2, 2):
            simp13_sum += (4 * fcn(i*h)) + (2 * fcn(h*(i+1)))
        simp13_sum += (4 * fcn(h*(n-1)) + fcn(h*n))
        return (h * simp13_sum / 3)
    # Step height across the function
    height = (u_bnd - l_bnd)/n_point
    # Instantiate a variable to hold sum of the total integral
    st_int = 0
    # Check for application of trapezoid method
    if n_point == 1:
        st_int = trap(height, fcn(0), fcn(1))
    else:
        # Stores a mutable version to hold number of points
        m_point = n_point
        # Determine if the number of points is odd
        odd = n_point/2 - int(n_point/2)
        if (odd > 0) and (n_point > 1):
            # The number of points is even, so use 3/8ths rule on the last 4 points
            st_int += simp_38(height, fcn(height*(n_point-3)), fcn(height*(n_point-2)), fcn(height*(n_point-1)), fcn(height*n_point))
            # Update the number of points to use 1/3rd rule on
            m_point = n_point - 3
        if m_point > 1:
            # feed the rest of the points to Simpson's third
            st_int += simp_13m(fcn, height, m_point)
    return st_int

def sim_int_num(x_list, y_list):
    '''
    Numerical Methods : Integration
    Numerically integrates an xy list using an optimized simpson algorithm
    '''
    hgt = abs(x_list[0]-x_list[1])
    n_sz = len(x_list)
    odd = abs(n_sz/2 - int(n_sz/2))
    m_cnt = n_sz
    st_int = 0
    trap = lambda h, f_0, f_1 : h * (f_0 - f_1) / 2
    def simp13(h, f_0, f_1, f_2):
        return 2*h*(f_0 + 4*f_1 + f_2)/6

    def simp_38(h, f_0, f_1, f_2, f_3):
        '''
        Simpson's 3/8ths rule: Approximates a 3rd order Lagrange
        polynomial fit to four points.
        '''
        return (3*h * (f_0 + 3* (f_1 + f_2) + f_3) / 8)


    def n_simp_13m(in_list, h, n=0):
        '''
        Simpson's 1/3rd rule: Multiple Application: Feed a function,
        height and number of points. Needs odd number of points
        '''
        if n == 0:
            n = len(in_list)
        simp13_sum = in_list[0]
        for i in range(1, n-2, 2):
            simp13_sum += (4 * in_list[i-1]) + (2 * in_list[i])
        simp13_sum += (4 * in_list[n-2]) + (in_list[n-1])
        return (h * simp13_sum / 3)
    if n_sz < 2:
        print('Insufficient points passed to Numeric Integrator for Datasets : sim_int_num\n 2 data points minimum required.')
    if n_sz == 2:
        st_int = trap(hgt, y_list[0], y_list[1])
    if odd > 0 and n_sz > 3:
        st_int += (simp_38(hgt,y_list[-4], y_list[-3], y_list[-2], y_list[-1]))
        m_cnt = n_sz - 3
    if m_cnt > 1:
        st_int += n_simp_13m(y_list, hgt, m_cnt)
    # for i in range(1,m_cnt-1,2):
    #     # st_int += simp13(hgt, y_list[i], y_list[i+1], y_list[i+2])
    #     st_int += n_simp_13m(y_list, hgt, m_cnt)
    # # print(st_int)
    return st_int






def ex21_6():
    func = lambda x : 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
    low = 0
    high = 0.8
    n_seg = 100
    x_vals = np.linspace(low, high, n_seg)
    y_vals = np.array(func(x_vals))
    snum = sim_int_num(x_vals, y_vals)
    print(snum)
    print(sim_int(func, low, high, n_seg))
ex21_6()
