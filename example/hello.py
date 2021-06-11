

'''1.基本输入输出'''
import sys

print('你好')
# 2. \ 转义字符，把一些字符转化成特殊字符。
print(' 输出单引号：\' \n 输出双引号：\" \n 输出反斜杠：\\ ')
# 3.输入 input 函数， 语法： 变量 = input(提示字符串)。
name = input('请输入你的姓名：')
print('输入的姓名为：%s' %(name))               # % 方式动态输出 ， {} format 形式输出。
print('输入的姓名为：{}'.format(name))          # 两者是等价的


print('\\')
# 一、print 函数的使用
# 1. print("项目"%(参数行) )  项目中使用
# %s   -->    字符串
# %d   -->    整数
# %f   -->    浮点数
name = "JackYang"
number = 100
smallNumber = 100.25
age = 108
print('%s\n%d\n%f'%(name,number,smallNumber))
print("%s的年龄是%d岁！"%(name,age) )

# 2.使用format()进行格式化输出
print('{}的年龄是{}岁！'.format(name,age))

# 二、input 函数的使用
# 语法 ：变量 = input(提示字符串)  当我们按回车键后就会将输入的数据赋值给变量。eg：
height = input('请输入你的身高：')
print(height)
# 注：input 所输入的内容是一种字符串，如果要将该字符串转化成整数，则使用int()或eval()，如转成浮点数，则必须使用float()

pi = 3.1415926
r = float(input("请输入圆的半径："))
print('圆的周长是：',2 * pi * r)

print('%d'%(30))      # 11110
print('%o'%(30))      #36
print('%x'%(30))      #1e
print('%X'%(30))      #1E

# 三、运算符与表达式
# 表达式是由运算符与操作数所组成的。其中+、-、*及/符号称为运算符，操作数则包含变量、数值和字符。

# 1.算术运算符
# 与C语言相比多了一个幂次运算符
# 2.复合赋值运算符
# 与c语言类似
# 3.关系运算符
# 用来比较两个数值之间的大小关系，通常用于流程控制语句，若运算结果成立则返回真值(True);若不成立，则返回假值(False)。
# 注意：Python中的Boolean类型是True和False，即首字母大写，与Java不同。
# 4.逻辑运算符
# and(与) or(或) not(非)
print(100 > 2) and (1 > 41) #False   此时输出的是第一个小括号计算出来的值
total = 124
value = (total % 4 == 0) and (total % 3 == 0)
print(value)         # 输出为 False  说明：and(与) 的优先级 > 赋值 ，因此上述不需要加括号
# 5. 位运算符
# 就是将二进制逐位进行运算。在Python中，如果要将整数转换为二进制，就可以使用内置函数bin()。与C语言差不多
print(10,bin(10))      # 0b1010
print(5,~5)            # 00101  --> 11010
print(sys.getsizeof(5))
# 三、流程控制
# 3种流程控制结构，即if、for、while
# if 条件表达式1：
# #     语句块1
# # elif 条件表达式2：
# #     语句块2
# # ...
# # else:
# #     语句块
# 与C语言比较 把else if 简写成 elif；把用()表示的条件表达式改成：条件表达式:和缩进替代，更加简单eg:
# 输入两个数a,b,输出其中的最大数。
a = eval(input('请输入一个数：'))
b = eval(input('请再输入一个数：'))
if a > b :
    print(a)
elif a < b :
    print(b)
else :
    print('{}等于{}'.format(a,b))

# for 循环：
# for 循环又称计数循环，是一种可以重复执行固定次数的循环，语法如下：
#     for item in 序列对象:
#         for 的语句块
#     else:
#         的语句块 # 可加入也可不加入
'''上述语句可以不加入else指令。Python中提供有 range() 函数来搭配使用，主要功能是建立整数序列，语法如下:
range([初始值],[终值],[步长])
返回一个等差数列的可迭代对象，不包括终值，这里[]表示可选项。初始值的默认值为0，步长的默认值为1。可迭代对象，必须转化为
列表才能显示所有元素。'''
# eg:求1到100的和
sum = 0
for item in range(1,101):       #注意；range()函数是左开右闭区间
    sum += item
print('sum=',sum)
# 2020 1020