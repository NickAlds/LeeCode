"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""
# 链表节点定义
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    # 迭代
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = head
        if not head:
            return head
        while head.next:
            next1 = head.next
            head.next, next1.next = head.next.next, new_head
            new_head = next1
        return new_head
    # 递归
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head, head)
    
    def reverse(self, head, tail):
        if not tail or not tail.next:
            return head
        else:
            new_head = tail.next
            tail.next = tail.next.next
            new_head.next = head
            return self.reverse(new_head, tail)
    
    def reverseList2(self, head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, prev.next
        return prev