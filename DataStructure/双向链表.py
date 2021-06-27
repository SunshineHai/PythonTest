
class ListNode(object):
    # 1.定义构造器
    def __init__(self, val = 0):
        self.prev = None   # 前指针
        self.val = val      # 存放值
        self.next = None    # 后指针

class MyLinkedList(object):
    # 1.构造器: 初始化头结点
    def __init__(self):
        self.size = 0  # 节点个数
        # 头结点 和 尾节点
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # 2. 定义 append() : 用来添加节点
    def append(self, val: list) -> bool:
        # 1.列表长度为0，添加失败
        if len(val) == 0:
            return None
        # 2.开始添加
        temp = self.head  # temp 指向头结点
        for x in val:
            node = ListNode(x)
            # 连接头结点
            temp.next = node
            node.prev = temp
            # 连接尾节点
            node.next = self.tail
            self.tail.prev = node
            # temp 指向当前元素
            temp = temp.next    # 添加完节点之后，temp指向最新的节点
            self.size += 1
        return self.head     # 添加完元素后，最后返回头结点

    # 3.定义out() : 输出添加的节点的所有值
    def out(self):
        # 问题 ： 怎样把尾节点 tail 不输出？
        # 注意：判断 temp != None  和 temnp.next != None 的区别
        # 1.如果头结点为空，返回None
        if self.head.next == None:
            return None
        temp = self.head.next  # 相当于指向第一个元素
        while temp.next != None:
            print(temp.val)
            temp = temp.next  # temp 指向下一个节点
        return True

    # get(index) : 得到 index 索引 对应的 节点值
    def get(self, index : int):
        if index < 0 or index >= self.size:
            return -1
        # 迭代
        temp = self.head
        for _ in range(index+1):
            temp = temp.next
        return temp.val

    # 4.插入节点
    def addAtIndex(self, index : int, val : int) -> None:
        # Add a node of value val before the index-th node in the linked list.
        # 对于 索引 index = size 时，插入就会报错，增加尾节点就可以神奇的解决，而且不需要单独考虑这种插入情况了
        if index > self.size:
            return None

        if index < 0:
            index = 0

        node,  temp= ListNode(val), self.head
        for _ in range(index + 1):  # 遍历找到index对应的元素
            temp = temp.next
        node.next = temp
        node.prev = temp.prev
        node.prev.next = node
        self.size += 1

        return True
     # 5.删除
    def deleteAtIndex(self, index : int):
        if index < 0 or index >= self.size:
            return
        # 迭代定位到 index 对应的节点
        temp = self.head
        for _ in range(index + 1):
            temp = temp.next
        print('a:', temp.val)
        # begin delete
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

        self.size -= 1
        return None

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

if __name__ == '__main__':
    obj = MyLinkedList()
    my_list = [1, 2, 3, 4, 5, 6]
    obj.append(my_list)
    print('节点的长度：{0}'.format(obj.size))
    # obj.out()
    index = 4
    val = 1314
    obj.addAtIndex(index, val)
    obj.out()
    print('Now : 节点的长度：{0}'.format(obj.size))

    obj.deleteAtIndex(4)
    obj.out()

    print('get({0}) = {1}'.format(index, obj.get(index)))

    obj.addAtHead(521)
    obj.out()

    obj.addAtTail(521)
    obj.out()