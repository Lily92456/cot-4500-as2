import numpy as np

# Problem 1 - Neville's Method
def neville_interpolation(x, y, x_interp):
    n = len(x)
    Q = np.zeros((n, n))
    Q[:, 0] = y  # 1st column is only y values
    
    for j in range(1, n):
        for i in range(n - j):
            Q[i, j] = ((x_interp - x[i + j]) * Q[i, j - 1] - (x_interp - x[i]) * Q[i + 1, j - 1]) / (x[i] - x[i + j])
    
    return Q[0, n - 1]

x_values = [3.6, 3.8, 3.9]
y_values = [1.675, 1.436, 1.318]
x_interp = 3.7

# Problem 1 Function call
neville_result = neville_interpolation(x_values, y_values, x_interp)
print(neville_result)




# Problem 2: Newton's Forward Difference Method





