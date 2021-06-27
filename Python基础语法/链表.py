
# 链表: 定义节点
class Node(object):
    # 定义构造器，初始化链表中的指针域和数据域。
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class ListNode(object):
    head = Node()  # 头节点固定不动
    def __init__(self, val = None):
        self.append(val)

    # 定义 append() : 添加元素到链表中

    def append(self, ele):
        if ele == None:
            return self.head
        temp = Node()   # 用来移动的节点
        temp = self.head
        node = Node(ele)
        # 找到节点的最后一个元素。
        # while True:
        #     if temp.next == None:
        #         break
        #     temp = temp.next
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
    # 移除val : 迭代法
    def removeElements(self, val : int):
        temp = self.head
        while temp.next != None:
            if (temp.next.val == val):
                temp.next = temp.next.next
                # 末尾
            else:
                temp = temp.next

if __name__ == '__main__':
    node = ListNode()
    node.append(1)
    node.append(2)
    node.append(6)
    node.append(3)
    node.append(4)
    node.append(5)
    node.append(6)
    node.removeElements(6)
    node.output()