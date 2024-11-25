import numpy as np


def M_w(wA, wB, xA, xB):
    return 1 / (1 + np.exp(-(wA * xA + wB * xB)))

data = np.array([
    [1.0, 1.3, 0],
    [2.2, 1.1, 1],
    [2.0, 2.4, 1],
    [1.5, 3.2, 0],
    [3.2, 1.2, 1]
])

xA = data[:, 0]  
xB = data[:, 1]  
y = data[:, 2]   


wA_vertex = np.arange(0, 1.1, 0.1)
wB_vertex = np.arange(2, 3.1, 0.1)

result_matrix = np.zeros((len(wA_vertex), len(wB_vertex)))

for i, wA in enumerate(wA_vertex):
    for j, wB in enumerate(wB_vertex):
        
        M_w_values = M_w(wA, wB, xA, xB)
        
        
        mse = np.sum((y - M_w_values) ** 2) / M_w_values.size
    
        
        result_matrix[i, j] = mse

print("result:")
print(result_matrix)