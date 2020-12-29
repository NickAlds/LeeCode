class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        sum_list = l1
        while l1.next or l2.next:
            l1.val = (l1.val + l2.val + carry)%10
            carry = (l1.val + l2.val + carry)//10
            l1 = l1.next
            l2 = l2.next

