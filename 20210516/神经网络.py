import numpy as np
import matplotlib.pylab as plt
# 因为感知机中权重的设置是人为的，这是一个缺点，下面介绍的是神经网络就是从数据中学习权重来解决感知机的问题。

# 1. 感知机中使用的是函数称为"阶跃函数"，若将阶跃函数换成其他函数则变成神经网络了。

# 2.神经网络中常用的激活函数：sigmoid 函数 ： h(x) = 1 / (1 + e ^ -x)

# 使用Python画出阶跃函数：

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function(x):
    y = x > 0
    return y.astype(np.int)

x = np.array([-1.0, 1.0, 2.0])
print(x)
y = x > 0
print(y)
# 将numpy数组中的布尔型转换成int型
y = y.astype(np.int)
print(y)

# 1. 阶跃函数的实现
def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #指定y轴的范围
plt.show()

# 2.sigmoid 函数的实现
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
x = np.array([-1.0, 1.0, 2.0])
y = sigmoid(x)
print(y)

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.show()

t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
print(1.0/t)

# x = np.arange(0, 2 * np.pi, 0.1)
# y = np.sin(x)
# plt.plot(x ,y)
# plt.show()

# ReLU 函数

def relu(x):
    return np.maximum(0, x)

x = np.arange(-6, 6, 0.1)
y = relu(x)
plt.plot(x, y)
plt.show()

