# 链表: 定义节点
class ListNode(object):
    # 定义构造器，初始化链表中的指针域和数据域。
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        """
           Initialize your data structure here.
        """
        self.size = 0              # 成员变量：存放结点的个数
        self.head = ListNode(0)     # 成员变量：头结点
    # size() : 返回 size
    def getSize(self):
        return self.size

    # 定义 append() : 添加元素到链表中
    def append(self, ele : list):
        if ele == None:
            return
        self.size = len(ele)
        # 用来移动的节点
        temp = self.head
        for e in ele:
            node = ListNode(e)
            # 找到节点的最后一个元素。
            while temp.next != None:
                temp = temp.next
            temp.next = node
        return self.head
    # 输出节点
    def output(self):
        if self.head.next == None:
            print('这个链表为空')
        head = self.head.next
        while head != None:
            print(head.val)
            head = head.next

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # 1.判断索引是否在结点中
        if index >= self.size:
            return -1

        if index < 0:
            index = 0

        temp = self.head    # temp 指向头结点
        # 2.开始查找结点
        for _ in range(index + 1):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        return None

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        return True

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # 1.判断索引的位置是否符合条件
        if index < 0 or index > self.size:
            return None
        temp = self.head    # temp 指向头结点
        # 2.找到要插入节点位置的前一个位置
        for _ in range(index):
            temp = temp.next
        # 遍历结束得到要插入索引位置的前一个元素
        # 3.插入节点
        node = ListNode(val)
        node.next = temp.next
        temp.next = node

        self.size += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return -1
        temp = self.head    # temp 指向头结点
        # 1.遍历找到index-1索引对应的值
        for _ in range(index):
            temp = temp.next
        # 2.删除元素
        temp.next = temp.next.next
        self.size -= 1
        return None


# Your MyLinkedList object will be instantiated and called as such:
if __name__ == '__main__':

    my_list = [1, 2, 6, 3, 4, 5, 6]
    obj = MyLinkedList()
    obj.append(my_list)
    # obj.output()
    print('size : {0}'.format(obj.getSize()))
    index = 1
    param_1 = obj.get(index)
    print('get({0}) = {1}'.format(index, param_1))
    obj.size
    val = 521
    # obj.addAtHead(val)
    # obj.output()
    # obj.addAtTail(val)
    # obj.output()
    # obj.addAtIndex(index, val)
    # obj.output()

    obj.deleteAtIndex(2)
    print('the length after delete : ', obj.size)
    obj.output()


