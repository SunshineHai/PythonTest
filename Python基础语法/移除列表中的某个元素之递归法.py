
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
    def append(self, ele : list):
        if ele == None:
            return self.head
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

    # 移除val : 递归法, 递归太难懂了，存储空间过高，不推荐使用
    def removeElements(self, head, val : int):
        if head == None:
            return head
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head
if __name__ == '__main__':
    node = Solution()
    head = node.append([1, 2, 6, 3, 4, 5, 6])
    # node.append(4)
    # node.append(5)
    # node.append(6)
    node.head = node.removeElements(head, 6)
    node.output()


