"""
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        flag = True
        start = head
        start_node = ListNode(0)
        start_node.next = head
        while start_node.next:
            tmp_list = list()
            full = True
            for _ in range(k):
                if head:
                    tmp_list.append(head)
                    head = head.next
                else:
                    full = False
                    break
            
            if not full:
                break
            if flag:
                start = tmp_list[-1]
                flag = False
            tmp = tmp_list[-1].next
            for node in reversed(tmp_list):
                start_node.next = node
                start_node = node
            start_node.next = tmp
        return start