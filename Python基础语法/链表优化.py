
# 链表: 定义节点
class ListNode(object):
    # 定义构造器，初始化链表中的指针域和数据域。
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    head = ListNode()
    def __init__(self, val = None):
        self.append(val)

    # 定义 append() : 添加元素到链表中
    def append(self, ele):
        if ele == None:
            return self.head
        # 用来移动的节点
        temp = self.head
        node = ListNode(ele)
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

    # 移除val : 迭代法
    def removeElements(self, head, val : int):
        if head == None:
            return head
        temp = ListNode()
        temp = head
        while temp.next != None:
            if (temp.next.val == val):
                temp.next = temp.next.next
                # 末尾
            else:
                temp = temp.next
        return head
if __name__ == '__main__':
    node = Solution()
    node.append(7)
    node.append(7)
    node.append(7)
    node.append(7)
    # node.append(4)
    # node.append(5)
    # node.append(6)
    node.removeElements(node.head, 7)
    node.output()


