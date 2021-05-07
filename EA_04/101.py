import numpy as np

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