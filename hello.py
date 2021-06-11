# 1. 求 1 到 5 的和：
sum = 0
for i in range(1, 5):
    sum += i
print(sum)
# pandas 库 ： 是一个基于Numpy开发的更高级的结构化数据分析工具，提供了Series、DataFrame、Panel等数据结构，可以很方便地对序列、
# 截面数据（二维表）、面板数据进行处理。
'''
1.pandas 用来处理表格或异质性数据
2.Numpy 适合处理同质性的数值类数组数据
'''
import pandas as pd
import numpy as np
from pandas import Series, DataFrame  # 常用这两个类

# print (pd.show_versions())   # 打印出各个包的版本号

csv = pd.read_csv('E:\Data\sample.csv',encoding = 'gbk')
print(csv)

obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.index)
print(obj.values)

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)
print(obj2['a'])
obj2['d'] = 6
print(obj2[['c', 'a', 'd']])
print(obj2[obj2 > 0])
print(obj2 * 2)

print(np.exp(obj2)) # np.exp()函数是求 e的x次方 的值的函数。
# 使用 pandas 读取Excel表格信息
xlsx = pd.read_excel('E:\Data\sample.xlsx', sheet_name='Sheet1')
print(xlsx)

#2.读取纯文本、CSV、PDF、Word文档
#2.1 纯文本


#SymPy 工具库的使用

from sympy import *

var_x = symbols('x')

print(var_x)

from sympy import *
x,y,z = symbols('x  y  z')
#1.例1
m0,m1,m2,m3 = symbols('m0:4')  #创建多个符号变量
x = sin(1)
print("x=",x)
print("x=",x.evalf())
print("x=",x.n(16))  #显示小数点后16位数字
print("pi的两种显示格式:{},{}".format(pi,pi.evalf(3)))  #这里不能使用n()函数
#2.例2
expr1 = y * sin(y**2)  #创建第一个符号表达式
print(expr1)
expr2 = y ** 2 + sin(y) * cos(y) + sin(z)  #创建第二个符号表达式
print("expr1=",expr1)
print("y=5时，expr1=",expr1.subs(y,5))  #代入一个符号变量的值
print("y=2,z=3时，expr2=",expr2.subs({y:2,z:3}))  #代入y=2,z=3
print("y=2,z=3时，expr2=",expr2.subs({y:2,z:3}).n())  #以浮点数显示计算结果
