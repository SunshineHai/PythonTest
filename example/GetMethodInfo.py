
# 目的：输出正比例函数的图像：
# 格式化 ： ctro + alt + l
import math

import matplotlib.pyplot as plt
import numpy as np
# x = [0,1,2,3,4,5,6,7,8,9,10]            # 手動定義列表
# y = [math.sin(t) for t in x]            # 动态求出 y = sin(x) 的值赋值为列表

x = np.linspace(-10, 10, 1000)          #分别代表最小、最大，数量，生成一个等差数列
y = x

plt.plot(x, y)      #x， y是两个列表
plt.show()

print(np.pi);       #numpy 包里直接有可以调用pi

