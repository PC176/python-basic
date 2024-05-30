from numpy import *
m = matrix('11,12,13;21,22,23;31,32,33')
print(m)
print(m.min())
print(m.max())
print(diagonal(m))
print(m.flatten())
print(m.reshape(9,1))