
'''Python 3 -- 循环语句
1.while 循环
2.for 循环
注：Python 中没有do...while 循环
'''
'''1.while 循环
    1).一般格式：
while 判断条件(condition):
      执行语句(statement)...
    2).while 循环语句 else 语句
语法格式： while <expr>:
            <statements>
         else :
            <additional_statements>          
'''
sum,i = 0,1
while i <= 100 :
    sum += i
    i += 1   # Python 中没有 i++
print('1 到 100 的和为：%d' % sum)
# %d : 用作占位符 ,动态替换，与C语言中有所区别

var = 1
while var <= 1 :        # 若条件语句永远为 True,则为死循环，尽量避免
    num = int(input('请输入一个数字：'))
    print('你输入的数字为：', num)
    var += 1
# while ... else 语句
sum,i = 1,1
while i < 5 :
    print(i,'小于5')
    sum *= i
    i += 1
else :
    print('退出循环后i的值为：',i)
print('The value of sum is ',sum)
# 如果 while 后面的"执行语句"只有一行，可以与 while 写在同一行。eg:
flag = 1
# while(flag) : print('欢迎观看我的笔记！')  # 这是死循环，看不到下一句的执行
# print('这是结尾。。。')
'''2.for 循环
1).一般格式 ：
    for <variable> in <sequence> :
        <statements>
    else :
        <statements>
 2)range() 函数的使用：遍历数字

'''
#eg:
languages = ['C','C++','Java','Python']  # 使用 for 循环 遍历 list
for x in languages :
    print(x)
str = 'China is a great country.'
for x in str :
    print(x)
'''注意：break 和 continue 的区别
1.break ： 遇到 break，直接跳出当前循环
2.continue ： 只是跳出本次循环，下个元素还会执行循环
'''
sites = ['baidu','alibaba','tencent','JD','baidu','google','facebook']
for site in sites :
    if site == 'baidu' :
        print('百度')
        break    # 换成 continue 试试结果有什么不一样
    else :
        print('循环数据：' + site)
else :
    print('没有循环数据')
print('完成循环')                   # Result: 百度  完成循环

n = 5
while n > 0 :
    n -= 1
    if n == 2 :
        continue   # 换成 continue
    print(n)
print('循环结束')
# 4                 4
# 3                 3
# 循环结束           1
#                   0
#                   循环结束

'''range(num1 , num2,步长n) 函数：从num1 开始，每隔步长n,进行输出，左闭右开
步长可以是负数
 '''
for i in range(5,9) :
    print(i,end= ' ')  # result : 5 6 7 8
print()
for i in range(0,10,5) :
    print(i,end= ' ')
for i in range(-10,-100,-20) :
    print(i)
print(len(site))
for i in range(5) :  # 从 0 输出到 4
    print(i)
公司 = ['Google','Baidu','Alibaba','Tencent']
for i in range(len(公司)) :
    print(i,':',公司[i])   # Result ：
# 0 : Google
# 1 : Baidu
# 2 : Alibaba
# 3 : Tencent

'''也可以使用 range() 函数 创建一个  列表'''
print(list())
print(list(range(5)))

'''pass 语句 ： 空语句
pass 语句 不做任何事情，一般用作占位语句
'''
while True :
    pass   # 等待键盘中断

ch = 'A'

if ch >= 'A' and ch <= 'Z' :
    print(ch,'是大写字母')
elif ch >= 'a' and ch <= 'z' :
    print(ch,'是小写字母。')
else :
    print(ch,'既不是大写字母，也不是小写字母')

''' if 语句:
if 条件表达式1：
    语句块1
elif    条件表达式2：
    语句块2
elif 条件表达式m:
    语句块m
else:
    语句块 m+1    
 '''
# 例1.输入两个数a,b,输出其中最大数。
print('请输入两个数a和b:')
a = eval(input());
b = eval(input())
if a >= b :
    print('最大的值为：',a)
else :
    print('最大的值为：',b)

