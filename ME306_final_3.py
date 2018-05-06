from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
from NumericalMethods import ode45py

def me306_final_3():
    G = 9.8  # gravity m/s^2
    L1 = 1  # length pendulum 1 m
    L2 = 2  # length pendulum 2 m
    M1 = 2  # mass pendulum 1 kg
    M2 = 1  # mass pendulum 2 kg
    # t1_0 = 0.1 # Initial value for theta 1 displacement
    # w1_0 = 0 # Initial value for angular velocity
    # t2_0 = 0.17 # Initial value for theta 2 displacement
    # w2_0 = 0 # Initial value for angular velocity
    t1_0 = np.pi # Initial value for theta 1 displacement
    w1_0 = 0 # Initial value for angular velocity
    t2_0 = np.pi # Initial value for theta 2 displacement
    w2_0 = 0 # Initial value for angular velocity
    i_theta = np.array([w1_0, t1_0, w2_0, t2_0])
    def double_pend(t, theta):
        # Initialize the return variable
        dydx = np.zeros(4)
        #
        dydx[0] = theta[1]
        dydx[2] = theta[3]
        d_0 = theta[2] - theta[0]
        sA = (M1+M2)*L1
        sB = M2*L2*cos(d_0)
        sC = M2*L1*cos(d_0)
        sD = M2*L2
        sE = -M2*L2*(theta[3]**2)*sin(d_0) - G*(M1+M2)*sin(theta[0])
        sF = M2*L1*(theta[1]**2)*sin(d_0) - G*M2*sin(theta[2])
        dydx[1] = (sF*sB - sD*sE) / (sB*sC - sD*sA)
        dydx[3] = (sE*sC - sA*sF) / (sB*sC - sD*sA)
        return dydx


    # i_theta = np.array([0.0, 0.1, 0.0, 0.17])
    # i_theta = np.array([0, np.pi, 0, np.pi])
    d_time = np.array([0,100])
    if i_theta[1] == np.pi:
        fig_name = '3b'
    else:
        fig_name = '3a'
    X, Y = ode45py(double_pend, d_time, i_theta)
    x0 = np.zeros(len(X))
    y0 = np.zeros(len(X))
    x1 = L1*sin(Y[:,0]) + x0
    y1 = -L1*cos(Y[:,0]) + y0
    x2 = L2*sin(Y[:,2]) + x1
    y2 = -L2*cos(Y[:,2]) + y1
    topX = (x0, x1)
    topY = (y0, y1)
    botX = (x1, x2)
    botY = (y1, y2)
    plt.plot(X,Y[:,0],label=r'$\Theta_1$')
    plt.plot(X,Y[:,2],label=r'$\Theta_2$')

    plt.xlabel('Time (s)')
    plt.ylabel('Angle (radians)')
    plt.title(fig_name + ' Angular Displacement')
    plt.legend()
    plt.savefig('ME399_prob_{}_disp.png'.format(fig_name),bbox_inches='tight')
    plt.show()


    plt.plot(x2,y2,label=r'$m_2$',c='C1')
    plt.plot(x1,y1,label=r'$m_1$',c='C0')
    # for i in range(len(X)):
    #     if i % 100 == 0:
    #         plt.plot((x1[i], x2[i]),(y1[i], y2[i]),c='C2')
    #         plt.plot((x0[i], x1[i]),(y0[i], y1[i]),c='C3')
    plt.xlabel('X - Axis (Horizontal)')
    plt.ylabel('Y - Axis (Vertical)')
    plt.title(fig_name + ' Mass Trajectory')
    plt.legend()
    plt.savefig('ME399_prob_{}_traj.png'.format(fig_name),bbox_inches='tight')
    plt.show()

me306_final_3()