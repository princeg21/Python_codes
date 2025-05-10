import numpy as np
import matplotlib.pyplot as plt
from sys import getsizeof as size 

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
dvalues = [0.1, 0.8, 1.9, 2.5, 2.7, 2.3, 1.8, 1.2, 0.9, 0.1]
C = np.array(cvalues) 
D = np.array(dvalues)
dot_product = np.dot(C, D) # Dot product of C and D
print("Dot product of C and D:", dot_product) # Print the result of the dot product
# print(cvalues, type(cvalues), id(cvalues), size(cvalues[0]))
# C = np.array(cvalues) 
# print(C,type(C),id(C), size(C[0]))
# print(len(C))
# plt.plot(C)
# plt.title("Plot of C values")
# plt.xlabel("Index")
# plt.ylabel("C values")
# plt.show()