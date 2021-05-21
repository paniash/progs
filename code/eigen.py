import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la

def matrix_builder(dims, diag_elements, non_diag_elements):
    matrix = [[0] * dims for _ in range(dims)]
    for i in range(dims):
        for j in range(dims):
            if i == j:
                matrix[i][j] = diag_elements

            elif (i == j+1) or (i == j-1):
                matrix[i][j] = non_diag_elements

    return np.array(matrix)

#%%
matrix = matrix_builder(10, 14, 1)
la.eigvals(matrix)
