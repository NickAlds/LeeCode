'''
328. Odd Even Linked List
Description  Submission  Solutions
Total Accepted: 59110
Total Submissions: 139587
Difficulty: Medium
Contributors: Admin
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddhead = ListNode(-1)
        evenhead = ListNode(-1)
        cur, odd, even = head, oddhead, evenhead
        flag = True
        while cur:
            if flag:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            if not cur.next:
                even.next = None
                odd.next = evenhead.next
                break
            cur = cur.next
            flag = not flag
        return head

class Solution1(object):
    def oddEvenList(self, head):
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)

after = Solution().oddEvenList(h)
while after:
    print after.val
    after = after.next
