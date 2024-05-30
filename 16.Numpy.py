# from numpy import *
# import numpy as np
# # # 1st way
# y = np.array([[1, 2, 3, 4, 5, 6], [3, 3, 4, 5, 3, 5]])
# print(y)
# print(y.ndim, y.shape, y.size, y.dtype, y.itemsize, y.nbytes)
# arr1 = array([1, 2, 3, 4, 5, 6, 7], float64)
# print(arr1)
# print(type(arr1))
# print(arr1.size)
# print(arr1.ndim)
# print(arr1.itemsize)
# -----------------------------------------------------------------------------------
# # 2nd way
# arr2 = linspace(0, 15, 16)
# print(arr2)
# arr2 = linspace(1, 15)
# print(arr2)
# arr2 = linspace(1, 15, 10)
# print(arr2)
# # 3rd way
# arr3 = logspace(1, 10)
# print(arr3)
# print("%.2f" % arr3[3])
# # 4th way
# arr4 = arange(1, 20, 2)
# print(arr4)
# # 5th way
# arr5 = zeros(5)
# print(arr5)
# # 6th way
# arr6 = ones(5)
# print(arr6)
# arr6 = ones(5, int)
# print(arr6)
# # copy a array
# arr = array([1, 2, 3, 4, 5, 6])
# arrc = arr
# print(arr)
# print(arrc)
# print(id(arr))
# print(id(arrc))
# # shallow copy
# arr = array([1, 2, 3, 4, 5, 6])
# arrc = arr.view()
# arr[2] = 10
# print(arr)
# print(arrc)
# print(id(arr))
# print(id(arrc))
# # deep copy
# arr = array([1, 2, 3, 4, 5, 6])
# arrc = arr.copy()
# arr[2] = 120
# print(arr)
# print(arrc)
# print(id(arr))
# print(id(arrc))
# # some numericals
# arr = arr + 5
# print(arr)
# print((arr))
# -------------------------------------------------------------
# import numpy as np
# a = []
# for i in range(0, 3):
#     a.append(input())
# arr = np.array(a)
# print(type(arr))
# print(arr)

# ---------------
# import numpy as np

# # Enter your code here. Read input from STDIN. Print output to STDOUT


# def array_split(i, r, c):
#     # Write your code below
#     x = np.arange(0, i)
#     print(x)
#     y = np.reshape(x, (r, c))
#     z = np.hsplit(y, (r, c))
#     a = z[0]
#     b = z[1]
#     print(a)
#     print(b)


# if __name__ == "__main__":
#     i = int(input())
#     r, c = list(map(int, input().split()))
#     array_split(i, r, c)


# import numpy as np
# x = np.arange(30).reshape(6, 5)
# print(x)
# res = np.vsplit(x, (2, 5))
# print(res)
# print(res[0], end='\n\n')
# print(res[1], end='\n\n')
# print(res[2])
# -----------------


# import numpy as np

# x = np.array([[-2],
#               [2]])
# y = np.array([[-3, 3]])
# print(x.dot(y))
# # ------------------
# import numpy as np

# x = np.array([[-2],
#               [2]])
# y = np.array([[-3, 3]])
# print(x + y)

# -----------------
# import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT


# def array_oper(num1, num2):
#     np.random.seed(100)
#     x = np.random.randint(num1, num2, size=30).reshape(5, 6)
#     print(x)
#     k = (np.cumsum(x, axis=0))
#     l = (np.cumsum(x, axis=1))
#     # print(k)
#     # print(l)


# if __name__ == "__main__":
#     num1 = int(input())
#     num2 = int(input())
#     array_oper(num1, num2)

# -----
import numpy as np

x = np.array([[0, 1], [1, 1], [2, 2]])
print(x.sum(-1))


x = np.arange(30).reshape(3, 5, 2)
print(x[-1, 2:-1, -1])

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x[[0, 1, 2], [0, 1, 1]])


x = np.arange(4)
print(x.flatten())


x = np.arange(12).reshape(3, 4)
print(x[:, 1])
