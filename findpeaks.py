def findpeaks(x_list, y_list, dy_list, d2y_list):
    '''
    Accepts lists of x values and y-values with numerically derived first and second derivatives
    returns list of indices for detected peaks. Requires filtered data.
    '''
    peak_points = []
    sign_toggle = 0
    n_pts = len(x_list)
    for x_i in range(n_pts):
        sign = sign_toggle
        if dy_list[x_i]*-1 > 0:
            # negative
            sign = 0
        else:
            sign = 1
        if sign != sign_toggle:
            sign_toggle = sign
            if d2y_list[x_i] < 0:
                peak_points.append(x_i)
    return peak_points