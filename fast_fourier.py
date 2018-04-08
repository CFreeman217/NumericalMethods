import math as math
def fast_fourier(in_list):
    n_size = len(in_list)
    n2_size = n_size
    m = math.log(n2_size)/math.log(2)
    for k in range(1,m + 1):
        n1_size = n2_size
        n2_size = n2_size/2
        angle = 0
        arg = 2 * math.pi / n1_size
        for j in range(n2_size):
            c = math.cos(angle)
            s = -math.sin(angle)
            for i in range(j, n_size, n1_size):



