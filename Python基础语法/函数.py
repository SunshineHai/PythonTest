# 注意：实参、形参中的地址不一致，str 是 不可变类型
def change(s : str):
    s = 'I love China!'
    print("函数中的形参的地址：{0}".format(id(s)))
    return s

s = "我是中国人: "
print("实参中的地址:{0}".format(id(s)))
print(change(s))

import numpy as np
print(np.cos(np.pi/5)) # 0.81

res = np.cos(np.pi/5)
a = 100
print(2 * 100 * res)

import numpy as np
a = np.random.randn(100, 100)
print(np.dot(a, a))