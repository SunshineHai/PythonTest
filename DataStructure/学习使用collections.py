from collections import Counter
import collections

# 计算列表中 每种元素出现的次数。
tree = [1, 2, 3, 2, 2]
print(Counter(tree))

count = collections.Counter
print(count)

# for 循环进行遍历
languages = ["C", "C++", "Java", "Python"]
print("列表：{0}".format(languages[0]))
for x in languages:         # 这个遍历的是 列表 ：languages
    print(x)

# 对于整数使用range()函数进行遍历
for i in range(5):          # 左闭右开
    print(i)
print("---------")
# range() 也可以指定区间
for i in range(5, 9):
    print(i)
print("range()里也可以有3个形参，最后一个形参是步长！")
for i in range(-10, -100, -30):
    print(i)

a = ['Google', 'BaiDu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):     # 这个遍历的是 整数
    print(i, a[i])


tree = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(tree)))
# [(1,Spring), ()] : 列表里面放元组
for i, j in enumerate(tree):
    print(i)
    print(j)
# 如果2个遍历i,j，则把列表中的元组进行遍历。
for i in enumerate(tree):
    print(i)
# 1个循环变量，只能遍历列表中的每个元组。
tree = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

count = collections.Counter()
print("count : ", count[2])
count[0] = 3
count[1] = 1
count[2] = 3
print("count的长度：{0}".format(len(count)))
for i in count:
    print(i, count[i])

array = [2, 3, 1, 2, 4, 3]
print(array[0])

array = []
if not array:
    print(True)
else:
    print(False)

s = ['A', 'D', 'O', 'B', 'E', 'C', 'O', 'D', 'E', 'B', 'A', 'N', 'C']

for i in enumerate(s):
    print(i)