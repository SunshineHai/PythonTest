# 2.显示图像
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("lena.jpg")  # 读入人像，读取相对路径
# img = imread("C:\\Users\\JackYang\\Pictures\\学校Logo\\logo.png") # 读取绝对路径
# plt.imshow(img);
plt.show();


# 2.3 感知机的实现


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7  # theta : 表示阈值
    tmp = x1 * w1 + x2 * w2  # x1和x2分别是神经元，w1/w2是各自的权重
    if tmp <= theta:
        return 0
    else:
        return 1


print(AND(0, 0))    # 0
print(AND(0, 1))    # 0
print(AND(1, 0))    # 0
print(AND(1, 1))    # 1
print("法一：%d"%(AND(0.5,0.5)))
# 2.3.2 导入权重和偏置
import numpy as np
x = np.array([0, 1])        # 输入
w = np.array([0.5, 0.5])    # 权重
b = -0.7    # 偏置
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x) + b)

def AND2(x1, x2):
    b = -0.7    # b ：偏置
    x = np.array([x1, x2])  # x ： 神经元
    w = np.array([0.5, 0.5])    # w : 权重
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print("法二：%d"%(AND2(0.5, 0.5)))

# 与非门 ： 偏置和权重与与门不同 (颠倒了与门的输出)
def NAND(x1, x2):
    b = 0.7    # b ：偏置
    x = np.array([x1, x2])  # x ： 神经元
    w = np.array([-0.5, -0.5])    # w : 权重
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print("-----与非门--------")
print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))
# 或门
def OR(x1, x2):
    x = np.array([x1, x2])  # x ： 神经元
    w = np.array([0.5, 0.5])    # w : 权重
    b = -0.2  # b ：偏置
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
print("-----或门--------")
print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))

# 2.4 感知机的局限性
# 单层感知机不能表示异或门
# 异或门可以通过组合来实现：
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
print("-----异或门--------")
print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))

# 以上异或门的实现，可以成为多层干感知机