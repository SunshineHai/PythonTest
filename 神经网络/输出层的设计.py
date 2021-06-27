import numpy as np
# 输出层的设计
# 神经网络可以用在分类问题和回归问题上
# 一般而言，回归问题用恒等函数，分类问题用softmax函数。

# 1.恒等函数：输出层原样输出，比较简单。

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)   # 指数函数
print(exp_a)

sum_exp_a = np.sum(exp_a)   # 指数函数的和
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
# 测试 ; 看到67页了
a = np.array([0.3, 2.9, 4.0])
print(softmax(a))

import matplotlib.pylab as plt
# 画出 softmax 函数图像
x = np.arange(-10, 10, 0.1)
y = softmax(x)
plt.plot(x, y)
# plt.show()    # 画出图像

# softmax 函数的优化
a = np.array([1010, 1000, 990])
# print(np.exp(a) / np.sum(np.exp(a))) # softmax 函数计算时报错：RuntimeWarning: invalid value encountered in true_divide
c = np.max(a)
print(a - c)
print(np.exp(a-c)/np.sum(np.exp(a-c)))
# 上例通过减去输入信号中的最大值，防止函数中的值为无穷大或者无穷下，导致计算机计算错误。

# 优化之后的 softmax(主要优化溢出)

def softmax(a):         # 形参传入的是numpy数组
    c = np.max(a)
    exp_a = np.exp(a-c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))

# 性质：
# 1.softmax 函数的输出是 0.0 到 1.0 之间的实数。
# 2.softmax 函数的输出值的总和是 1。故我们可以把softmax函数的输出解释为"概率"
# 机器学习问题的步骤可以分为：
# 1.学习 : 进行模型学习
# 2.推理 ： 用学到的模型对未知数据进行推理

