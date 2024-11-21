import numpy as np
array = np.random.rand(11)
print(array)

array = np.arange(10)
array_2 = np.reshape(array,(2,5))
print(array_2)

print(np.sum(array))
print(np.mean(array))
print(np.max(array))
print(np.min(array))
