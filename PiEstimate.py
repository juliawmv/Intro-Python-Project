{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "def pi(N,L,R):\n    # initializes variable for total points in the circle and arrays for x and y points within and outside of the circle\n    circle_sum = 0\n    not_in_circle = 0\n    circle_pointsx = []\n    circle_pointsy = []\n    square_pointsx = []\n    square_pointsy = []\n    for i in range(N):\n        # generates x and y points uniformly in a square that can be a set length\n        x = random.uniform(-L,L)\n        y = random.uniform(-L,L)\n        if x**2 + y**2 <= R:\n            # tests if points are within or on the circle in a set radius and adds them to a total\n            circle_sum = circle_sum + 1\n            # adds coordinates of points in the circle to arrays for plotting\n            circle_pointsx.append(x)\n            circle_pointsy.append(y)\n        if x**2 + y**2 > R:\n            # tests if points are not within the circle in a set radius and adds them to a total\n            not_in_circle = not_in_circle + 1\n            # adds coordinates of points outside of the circle to arrays for plotting\n            square_pointsx.append(x)\n            square_pointsy.append(y)\n    # calculation to estimate pi\n    pi_estimate = 4 * (circle_sum/N)\n    return pi_estimate",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 1
    }
  ]
}