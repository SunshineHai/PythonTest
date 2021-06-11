# 神经网络的学习
# 这里的"学习" 指的是从 训练数据中自动获得最优权重参数的过程。

# 损失函数 : 均方误差 和 交叉熵误差
# 1.均方误差
import numpy as np

y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t) ** 2)

ans = mean_squared_error(np.array(y), np.array(t))
print(ans)

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
ans = mean_squared_error(np.array(y), np.array(t))
print(ans)
# 得到的值越小，则均方误差越小，输出结果和监督数据更加吻合。
import matplotlib.pyplot as plt
# 2.交叉熵误差（损失函数）
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
ans = cross_entropy_error(np.array(y), np.array(t))
print(ans)

# 3.mini-batch 学习 （看到了89页）

