class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        cur = head
        while l1 or l2:
            if l1 and l2:
                digit_sum = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            elif l1:
                digit_sum = l1.val + carry
                l1 = l1.next
            else:
                digit_sum = l2.val + carry
                l2 = l2.next
            carry = digit_sum//10
            cur.next = ListNode(digit_sum%10)
            cur = cur.next
        if carry:
            cur.next = ListNode(1)
        return head.next


