'''
445. Add Two Numbers II Add to List
Description  Submission  Solutions
Total Accepted: 12398
Total Submissions: 26990
Difficulty: Medium
Contributors: Admin
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        summ = self.list2int(l1) + self.list2int(l2)
        strsum = str(summ)
        start = ListNode(int(strsum[0]))
        node = start
        for i in strsum[1:]:
            node.next = ListNode(int(i))
            node = node.next
        return start
    def list2int(self, node):
        summ = 0
        while node:
            summ = 10*summ+node.val
            node = node.next
        return summ


