
class Test:
    # 定义方法
    def prt(self):      # self ：代表类的实例，代表当前对象的地址，而 self.class 则指向类。
        print(self)
        print(self.__class__)
t = Test()
t.prt()
# <__main__.Test object at 0x000002E0E7703520>
# <class '__main__.Test'>

# 类的方法：
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def set(self, weight = 60):
        self.__weight = weight

    def get(self):
        print(self.__weight)

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()
p.set()
p.get()

