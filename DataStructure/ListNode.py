# 链表: 定义节点

class ListNode(object):
    # 定义构造器，初始化链表中的指针域和数据域。
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next