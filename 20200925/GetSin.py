import math
from math import *  # 加载数学模块 math 的所有对象
# 1.使用 泰勒公式 求 sin(x) 的值，通项精确到1e-6

x = eval(input('请输入角度：'));          # 从键盘中输入的数据作为角度，整型,作为自变量x
x = math.radians(x)    # 调用math.radians() 方法，把角度转换为弧度

# print('对应的弧度为：',radian)
# print(abs(angle))       # abs() 函数 是取绝对值

n = 0
sum = a = x     # sum 是存放泰勒公式累加之后的值，a(i) 代表第 i 个通项的值

while abs(a) >= 1e-6 :
    a *= (- x ** 2)/(2 * n + 3)/(2 * n + 2)     # 由a(0) 递推求出 a(1)
    n += 1
    sum += a
print('x = {},sin(x) = {}'.format(x,sum))

# 数据科学领域5个最佳Python库
# Numpy/Scipy/Pandas/Matplotlib/Scikit-learn

