
# 字典(dictionary) :存放键值对

dict = {1 : 'A', 2 : 'B', 3 : 'C', 4 : 'd'}
print(dict.pop(1))
print(dict)
print(dict.get(1))
print(dict.get(2))

# 需求:如果我要删除某个key对应的value值，怎么办？
dict2 = {1 : 'DD'}
dict.update(dict2)
print(dict)

midStr = {'A' : 1, 'B' : 3, 'C' : 1}
# 怎样把key = 'B'的value 减一？

midStr.update({'B' : 2})
print(midStr)

dictionary = {}
print(dictionary.keys())
print(dictionary.values())

print(dict.keys())

s = "ABCEEABC"
subStr = {}
for i, j in enumerate(s):
    print(j, i)
    key = j
    if subStr.get(key) == None:
        subStr[key] = 1
    else:
        subStr[key] += 1
print(subStr)

# dict = {'A' : 10}
# dict.update({'B' : 2})
# print("Result:", dict.get('C'))
#
# # 这样进行赋值，好神奇
# dict['F'] = 100
# print(dict)

dict1 = {'A' : 2, 'B' : 4, 'D' : 1}
dict2 = {'B' : 1, 'A' : 1}
for key, value in dict1.items():
    print('key的值为{0}, value 的值为{1}'.format(key, value))

str = "ABC"
print(str[0])

str = 'ABCC'
dic = {}
for i, j in enumerate(str):
    if dic.get(j) == None:
        dic[j] = 1
    else:
        dic[j] += 1
print(dic)
dict = {'B' : 10, 'A' : 2}
print(dict.get('B'))

for end, str in enumerate(str):
    print(end, str)