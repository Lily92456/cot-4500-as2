import unittest
import numpy as np
from assignemnt_2 import neville_interpolation  

class TestInterpolationMethods(unittest.TestCase):
    
    def test_neville_interpolation(self):
        x_values = [3.6, 3.8, 3.9]
        y_values = [1.675, 1.436, 1.318]
        x_interp = 3.7
        expected_result = 1.554
        result = neville_interpolation(x_values, y_values, x_interp)
        self.assertAlmostEqual(result, expected_result, places=3)
    
    def test_newton_divided_differences(self):
        x = [7.2, 7.4, 7.5, 7.6]
        f = [23.5492, 25.3913, 26.8224, 27.4589]

        f_x0_x1 = (f[1] - f[0]) / (x[1] - x[0])  # 9.2105
        f_x1_x2 = (f[2] - f[1]) / (x[2] - x[1])  # 14.311
        f_x2_x3 = (f[3] - f[2]) / (x[3] - x[2])  # 6.365

        f_x0_x1_x2 = (f_x1_x2 - f_x0_x1) / (x[2] - x[0])  # 17.00167
        f_x1_x2_x3 = (f_x2_x3 - f_x1_x2) / (x[3] - x[1])  # -39.73

        f_x0_x1_x2_x3 = (f_x1_x2_x3 - f_x0_x1_x2) / (x[3] - x[0])  # -141.829

        self.assertAlmostEqual(f_x0_x1, 9.2105, places=4)
        self.assertAlmostEqual(f_x0_x1_x2, 17.00167, places=5)
        self.assertAlmostEqual(f_x0_x1_x2_x3, -141.829, places=3)
    
    def test_newton_interpolation(self):
        x_approx = 7.3
        x0 = 7.2

        f_x0 = 23.5492
        f_x0_x1 = 9.2105
        f_x0_x1_x2 = 17.00167
        f_x0_x1_x2_x3 = -141.829

        f_approx = (
            f_x0 +
            f_x0_x1 * (x_approx - x0) +
            f_x0_x1_x2 * (x_approx - x0) * (x_approx - 7.4) +
            f_x0_x1_x2_x3 * (x_approx - x0) * (x_approx - 7.4) * (x_approx - 7.5)
        )
        expected_value = 24.79356
        self.assertAlmostEqual(f_approx, expected_value, places=5)

if __name__ == "__main__":
    unittest.main()
