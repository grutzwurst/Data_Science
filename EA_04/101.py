import numpy as np

# 3. Create a 3x3 numpy array of all Trues
a = np.ones((3,3)).astype(bool)

# 4. How to extract items that satisfy a
# given condition from 1D array?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 != 0]

# 5. How to replace items that satisfy a condition
# with another value in numpy array?
arr[arr%2 != 0] = -1

# 8. How to stack two arrays vertically?
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c = np.concatenate((a, b), axis=0)
print(c)

# 9. How to stack two arrays horizontally?
d = np.concatenate((a, b), axis=1)
print(d)

print(np.intersect1d(a,b))
print(np.setdiff1d(a,b))
print(np.where(a==b))
print(a[(a < 5) & (a > 2)])

# 10. How to generate custom sequences
# in numpy without hardcoding?
a = np.array([1,2,3])
np.concatenate((np.tile(a, 3), np.repeat(a, 3)))

# 11. How to get the common items between
# two python numpy arrays?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a, b)

# 12. How to remove from one array those items
# that exist in another?
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
np.setdiff1d(a, b)

# 13. How to get the positions where elements
# of two arrays match?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a == b)

# 15. How to make a python function that handles
# scalars to work on numpy arrays?
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

def pair_max(a, b):
    idx_a_larger = np.where(a > b)
    result = b
    result[idx_a_larger] = a[idx_a_larger]
    return result.astype(float)

pair_max(a, b)

# 28. How to compute the mean, median, standard deviation
# of a numpy array?
url = 'https://archive.ics.uci.edu/' \
      'ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.genfromtxt(
    url, delimiter=',', dtype='float', usecols=[0])

stats = dict()
stats['mean'] = np.mean(sepallength)
stats['median'] = np.median(sepallength)
stats['deviation'] = np.std(sepallength)
print(stats)

# 29. How to normalize an array so the values range exactly
# between 0 and 1?
normalized = (sepallength-np.min(sepallength)) / \
             np.max((sepallength-np.min(sepallength)))
print(normalized)