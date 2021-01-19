# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lc_types import ListNode, print_linked_list, construct_linked_list
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = fast = slow = ListNode()
        dummy.next = head
        for _ in range(k-1):
            fast = fast.next
        # else:
        #    return head
        pre1, node1 = fast, fast.next
        fast = fast.next.next
        while fast and slow:
            fast = fast.next
            slow = slow.next
        pre2, node2 = slow, slow.next
        print(node1.val, node2.val)
        if node1 is node2:
            return dummy.next
        pre1.next, pre2.next = node2, node1
        node1.next, node2.next = node2.next, node1.next
        return dummy.next

if __name__ == '__main__':
    print_linked_list(Solution().swapNodes(construct_linked_list([1]), 1))

