def lin_reg(x_list, y_list):
    '''
    Generates linear regression best fit line for list of x-values and y-values passed in the form of a list
    Returns coefficients for the form y = a * x + b
    a, b, r_squared, std_er, er_max = lin_fit(x_list, y_list)
    a : a-coefficient
    b : intercept offset
    r_squared : correlation coefficient
    std_er : standard error
    er_max : maximum error
    '''
    # Gather information about the data set
    n = len(x_list)
    if n != len(y_list):
        print('Lists must be of equal length.')
        return
    s_xi = sum(x_list)
    s_yi = sum(y_list)
    y_mean = s_yi/n
    s_xi2 = sum([i**2 for i in x_list])
    s_xy = sum([x_list[i]*y_list[i] for i in range(n)])
    # Calculate coefficients
    coef_a = ((n * s_xy) - (s_xi * s_yi)) / ((n * s_xi2) - (s_xi**2))
    coef_b = ((s_xi2 * s_yi) - (s_xi * s_xy)) / ((n*s_xi2) - (s_xi**2))
    # Sum of the squares of residuals from the generated line
    s_sq_t = sum([((coef_a * x_list[i] + coef_b - y_list[i])**2) for i in range(n)])
    # Sum of the squares of residuals from the mean
    s_sq_r = sum([(y_list[i] - y_mean)**2 for i in range(n)])
    # Standard deviation
    st_dev = (s_sq_r / (n-1))**(0.5)
    # R-Squared Value - coefficient of determination
    r_sq = 1 - (s_sq_t / s_sq_r)
    # Standard error
    std_er = (s_sq_t/(n-2))**(0.5)
    # Find maximum error deviation from the best fit line
    er_max = max([abs(coef_a * x_list[i] + coef_b - y_list[i]) for i in range(n)])
    print('Linear Best Fit: y = ( {:.4f} ) x {:+.4f}'.format(coef_a,coef_b))
    print('Standard Deviation = {:.4f}'.format(st_dev))
    print('R-Squared, Calibration Constant = {:.4f}'.format(r_sq))
    print('Standard Error = {:.4f}'.format(std_er))
    print('Maximum Error = {:.4f}\n'.format(er_max))
    return coef_a, coef_b

def prob_3():
    deflect = [0.00, 1.25, 2.50, 3.75, 5.00]
    v_out = [0.10, 0.65, 1.32, 1.95, 2.70]
    m, b = lin_reg(deflect, v_out)


def ex17_1():
    y_i = [0.5,\
           2.5,\
           2.0,\
           4.0,\
           3.5,\
           6.0,\
           5.5]
    m, b = lin_reg([i for i in range(1,(len(y_i)+1))], y_i)


ex17_1()
prob_3()