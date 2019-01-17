"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
说明:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        p = new_head
        while p and p.next and p.next.next:
            frt = p.next
            snd = p.next.next
            frt.next = snd.next
            snd.next = frt
            p.next = snd
            p = frt
        return new_head.next