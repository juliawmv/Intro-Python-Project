def pi_estimate_3(N,L,R):
    '''
    Generates a square area and scatters random points within this area. Uses a defined circle based on square 
    length to calculate an estimate for pi based on the number of points in the circle versus total points as well
    as the size of the circle.
    
    Input: Total Points(N), Length of Square(L), and Radius of Circle(R)

    Output: Pi Esimate(pi_estimate)
    '''
    
    import random
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    
    # initializes variable for total points in the circle and arrays for x and y points within and outside of the circle
    circle_sum = 0
    not_in_circle = 0
    circle_pointsx = []
    circle_pointsy = []
    square_pointsx = []
    square_pointsy = []
    for i in range(N):
        # generates x and y points uniformly in a square that can be a set length
        x = random.uniform(-L,L)
        y = random.uniform(-L,L)
        if x**2 + y**2 <= R:
            # tests if points are within or on the circle in a set radius and adds them to a total
            circle_sum = circle_sum + 1
            # adds coordinates of points in the circle to arrays for plotting
            circle_pointsx.append(x)
            circle_pointsy.append(y)
        if x**2 + y**2 > R:
            # tests if points are not within the circle in a set radius and adds them to a total
            not_in_circle = not_in_circle + 1
            # adds coordinates of points outside of the circle to arrays for plotting
            square_pointsx.append(x)
            square_pointsy.append(y)
    # calculation to estimate pi
    pi_estimate = 4 * (circle_sum/N)
    return pi_estimate