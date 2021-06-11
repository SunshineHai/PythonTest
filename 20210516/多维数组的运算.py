import numpy as np

# NumPy 多维数组的运算
# 一维数组
A = np.array([1, 2, 3, 4])
print(A)

print(np.ndim(A))
print(A.shape)
print(A.shape[0])

# 二维数组 也称为 矩阵
B = np.array([[1,2], [3,4], [5,6]])
print(B)
print(np.ndim(B))   # 返回数组的维数
print(B.shape)      # 几行几列

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

print(A.shape)
print(B.shape)

print(np.dot(A, B)) #矩阵相乘的运算

A = np.array([[1,2], [3,1], [2,1]])
print(A.shape)
B = np.array([[1,0,1], [0,1,0]])
print(B.shape)
print(np.dot(A, B))

print(np.dot(B, A))

# C = np.array([[1], [2], [3]])
# print(np.dot(A, C))         # 3x2 和 3x1 的矩阵相称报错

A = np.array([[1,2], [3,4], [5,6]])
B = np.array([7,8])
print(np.dot(A, B))