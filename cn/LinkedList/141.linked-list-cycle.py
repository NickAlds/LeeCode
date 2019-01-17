"""
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

进阶：
你能用 O(1)（即，常量）内存解决此问题吗？
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            dhead = head.next
            while head and dhead:
                if head is dhead:
                    return True
                if not dhead.next:
                    break
                head = head.next
                dhead = dhead.next.next
        return False
