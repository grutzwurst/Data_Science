import numpy as np

# Create array
a = np.arange(10, 16)
print(a) # [10 11 12 13 14 15]

b = a.reshape(2, 3) # [[10 11 12], [13 14 15]]
print(b) # [[10 11 12], [13 14 15]]

c = np.array([[1,2,3], [4,5,6]])
print(c.shape) # (2, 3)
print(c.size) # 6

d = c[0].astype(float)
print(d) # [1. 2. 3.]
print(c[0,1]) # 2

e = np.arange(9).reshape(3, 3)
print(e.dot(d)) # [ 8. 26. 44.]
print(e @ d) # [ 8. 26. 44.]
print(d @ e) # [24. 30. 36.]
print(e*d) # [[ 0.  2.  6.], [ 3.  8. 15.], [ 6. 14. 24.]]

print(np.arange(5) * 3) # [ 0  3  6  9 12]
print(np.arange(5) + 3) # [3 4 5 6 7]
print(np.arange(5) ** 3) # [ 0  1  8 27 64]

rg = np.random.default_rng(1)
noise = rg.random((10, 10))
print(noise.shape) # (10, 10)

print(b > 11) # [[False False True], [ True  True  True]]