


a = [1, 2, 3, 4]
b = [1]
c = [1]
d = b
e = [1, "Hello world!", c, False]
print(id(b), id(c))                 # (194100040L, 194100552L)
print(id(b), id(d))                 # (194100040L, 194100040L)
print(b == c)                       # True
f = list("abcd")
print(f)                            # ['a', 'b', 'c', 'd']
g = [0]*3 + [1]*4 + [2]*2

a = [1, 0, 3, 4]
a.append(5)
print("使用append()方法：{0}".format(a))
a.reverse()
print(a)

g = a[::-1]
print(g)
a.sort()
print(a)
