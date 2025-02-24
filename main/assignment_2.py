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

# Given data points
x = [7.2, 7.4, 7.5, 7.6]
f = [23.5492, 25.3913, 26.8224, 27.4589]

# 1sdt divided differences
f_x0_x1 = (f[1] - f[0]) / (x[1] - x[0])  # 9.2105
f_x1_x2 = (f[2] - f[1]) / (x[2] - x[1])  # 14.311
f_x2_x3 = (f[3] - f[2]) / (x[3] - x[2])  # 6.365

# 2nd divided differences
f_x0_x1_x2 = (f_x1_x2 - f_x0_x1) / (x[2] - x[0])  # 17.00167
f_x1_x2_x3 = (f_x2_x3 - f_x1_x2) / (x[3] - x[1])  # -39.73

# 3rd divided difference
f_x0_x1_x2_x3 = (f_x1_x2_x3 - f_x0_x1_x2) / (x[3] - x[0])  # -141.829


print(f"f[x0, x1] = {f_x0_x1:.4f}")  # 9.2105
print(f"f[x0, x1, x2] = {f_x0_x1_x2:.5f}")  # 17.00167
print(f"f[x0, x1, x2, x3] = {f_x0_x1_x2_x3:.3f}")  # -141.829

# Problem 3 

# Given values
x_approx = 7.3
x0 = 7.2

# Previously computed divided differences
f_x0 = 23.5492
f_x0_x1 = 9.2105
f_x0_x1_x2 = 17.00167
f_x0_x1_x2_x3 = -141.829

# Compute the approximation
f_approx = (
    f_x0 +
    f_x0_x1 * (x_approx - x0) +
    f_x0_x1_x2 * (x_approx - x0) * (x_approx - 7.4) +
    f_x0_x1_x2_x3 * (x_approx - x0) * (x_approx - 7.4) * (x_approx - 7.5)
)

# Print the result
print(f"Approximated f(7.3) = {f_approx:.5f}")


# Problem 4







