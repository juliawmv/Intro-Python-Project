def Fit(x,y,dy):
    '''
    Generates a linear fit by determining the slope and y-intercept of an imported data set.

    Input: X Axis Data(x), Y Axis Data(y), Error On Y-Axis(dy)

    Output: Linear Fit (fit)
    '''
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    # initializes slope variables
    m_num = 0
    m_denom = 0
    
    # equations for variables used in slope/intercept calculations
    n = len(x)
    x_avg = np.mean(x)
    y_avg = np.mean(y)
    sy = np.sum(y/dy**2)

    # loop to generate numerator and denominator values for the slope calculation
    for i in range(n):
        m_num = m_num + ((x[i] - x_avg)) * ((y[i] - y_avg) - sy)
        m_denom = m_denom + ((x[i] - x_avg)**2)
    
    # equations for slope and intercept
    m = m_num/m_denom
    c = y_avg - (m * x_avg)

    # linear fit equation taking in the slope, intercept, and x values
    fit = m*x+c

    return fit