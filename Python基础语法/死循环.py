

# while True:
#     print(10)

array_list = [1, 3, 5]
# array_list.append()
print(array_list)


init_list = []
print(len(init_list) == 0)

for list in init_list:
    print(list == None)

print(init_list is None)

# 递归：求5的阶乘
def factoral(n : int) -> int:
    if n == 0:
        return 1
    else:
        return n * factoral(n-1)
print(factoral(5))

# list = [1, 2, 3]    # 定义列表变量时尽量不要使用 list 关键字，会引起冲突
str = 'foo'
str = list(str)
print(str)

