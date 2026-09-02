import numpy as np

## ------------Multidimensional Arrays ----------------
# array = np.array([[1, 2, 3, 4, 5], 
#                   [6, 7, 8, 9, 10], 
#                   [11, 12, 13, 14, 15],
#                   [16, 17, 18, 19, 20],
#                   [21, 22, 23, 24, 25]])

## ------------------Array Slicing ----------------
# print(array.shape)  # Get the shape of the array
# print(array[:, ::-1])  # Reverse the order of columns 
# print(array[::-1, :])  # Reverse the order of rows
# print(array[::-1, ::-1])  # Reverse the order of both rows and columns

## ----------------Math Operations -------------
# sure = np.array([1.01, 2.02, 3.03])

# # print(sure + 1)
# # print(sure * 2)
# # print(sure ** 2)
# # print(sure - 1)
# # print(sure / 2)
# # print(sure % 2)
# # print(sure // 2)

## -----------------Math Functions -------------
# print(np.sqrt(sure))
# print(np.round(sure))
# print(np.floor(sure))
# print(np.ceil(sure))
# print(np.exp(sure))
# print(np.log(sure))
# print(np.log10(sure))
# print(np.sin(sure))
# print(np.cos(sure))

## -----------------Array Operations -------------
# a = np.array([10, 20, 30])
# b = np.array([2, 4, 5])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

## -----------------Comparison Operations -------------
# scores = np.array([90, 80, 66, 44, 70])
# print(scores >= 60)

# scores[scores < 60] = 0
# print(scores)

## ------------------- Broadcasting -------------------
# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
# b = np.array([[10], [20], [30]])
# print(a.shape)
# print(b.shape)
# print(a + b)

# array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
# array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
# print(array1.shape)
# print(array2.shape)
# print(array1 * array2)

## ----------------- Statistical Functions -----------------
# a = np.array([[1, 2, 3, 4, 5],
#              [6, 7, 8, 9, 10]])
#
# print(np.average(a))
# print(np.sum(a, axis = 0))
# print(np.sum(a, axis = 1))
# print(np.mean(a))
# print(np.median(a))
# print(np.min(a))
# print(np.max(a))
# print(np.std(a))
# print(np.var(a))

## ----------------- Boolean Indexing (filtering) -----------------
# a = np.array([[10, 15, 20, 67, 69, 93, 20],
#               [25, 30, 35, 40, 45, 50, 55]])

# print(a[a > 20]) 
# print(a[a < 25])
# print(a[a % 2 == 0])

# print(np.where(a > 20 , a, 0))
# print(np.where(a < 25, a, 0))
# print(np.where(a % 2 == 0, a, 0))

# ----------------- Random Number Generation -----------------
# rng = np.random.default_rng(seed = 1)
# print(rng.integers(low=1, high=191, size=(3, 2)))
#
# np.random.seed()
# print(np.random.uniform(low=-1, high=5))


