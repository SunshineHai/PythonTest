'''学习目标：迭代器的使用          --2020.6.27
1.学会使用 迭代器 遍历 列表 和 集合
2.学会使用迭代器的 iter() 和 next() 方法

'''
list = [1,2,3,4]
it = iter(list)  # 创建 迭代器对象
print(next(it))
print(next(it))

print(list)
#1).使用 for 循环 遍历
'''迭代器只能往，不会后退'''
for x in it :
    print(x)
#2).使用 next() 函数 循环遍历
import sys
newList = [5,6,7,8]
it = iter(newList)
'''  报错：TypeError: 'list_iterator' object is not callable
第七行 使用 iter() 方法 创建的对象名字是 iter(我已经改成it)，第二次再使用iter() 方法时，它使用的时新声明的对象，
该对象没有这个方法不能调用
'''
print('---------------------')
while True :
    try :
        print(next(it))     # 使用异常处理，出现异常退出
    except StopIteration :
        sys.exit()
print('------分割线------')
