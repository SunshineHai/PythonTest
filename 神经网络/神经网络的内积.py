# 使用NumPy矩阵实现神经网络
# 通过矩阵的乘积进行神经网络的运算
import numpy as np
# X 代表神经元，W 代表权重 , 注意 X 和 W 的对应维度个数应相等
X = np.array([1,2])
print(X)
print(X.shape)

W = np.array([[1,3,5], [2,4,6]])
print(W)
print(W.shape)

A = np.array([1,2,3,4,5])
print(A.shape)      # 一维 ：输出一维数组的列数

Y = np.dot(X, W)
print(Y)

# 由此可以看出，通过矩阵的成绩一次性完成计算的技巧、在实现的层面上可以说是非常重要的。
