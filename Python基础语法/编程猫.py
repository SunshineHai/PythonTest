
# 1.编程猫
# name = input("what is your name:")
# print('Hello :', name)

#2.海龟作图

import turtle # 海龟
# t = turtle.Pen()
#
# t.forward(100)
# t.left(90)
#
# t.forward(100)
# t.left(90)
#
# t.forward(100)
# t.left(90)
#
# t.forward(100)
# t.left(90)

# 3.画五角星
len = 200   # 五角星边长
theta = 144 # 移动角度

t = turtle.Pen()    # 建画笔

# t.right(theta)      #向右移动theta角度
# t.forward(len)
#
# t.right(theta)
# t.forward(len)
#
# t.right(theta)
# t.forward(len)
#
# t.right(theta)
# t.forward(len)


# 4.for 循环

# for x in range(5):
#     t.forward(len)
#     t.right(theta)


# 由此可以看出，python 中函数支持不定参，对于调用函数时非常方便的。
# 画正方形：
for x in range(20, 160, 4):
    t.forward(x)
    t.right(90)

