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
      "source": "def DataFit(x,y,dy):\n    # initializes slope variables\n    m_num = 0\n    m_denom = 0\n    \n    # equations for variables used in slope/intercept calculations\n    n = len(x)\n    x_avg = np.mean(x)\n    y_avg = np.mean(y)\n    sy = np.sum(y/dy**2)\n\n    # loop to generate numerator and denominator values for the slope calculation\n    for i in range(n):\n        m_num = m_num + ((x[i] - x_avg)) * ((y[i] - y_avg) - sy)\n        m_denom = m_denom + ((x[i] - x_avg)**2)\n    \n    # equations for slope and intercept\n    m = m_num/m_denom\n    c = y_avg - (m * x_avg)\n\n    # linear fit equation taking in the slope, intercept, and x values\n    fit = m*x+c\n    return fit",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 1
    }
  ]
}