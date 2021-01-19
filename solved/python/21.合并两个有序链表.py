#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# @lc code=start
# Definition for singly-linked list.
from lc_types import ListNode, construct_linked_list, print_linked_list

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            # print_linked_list(l1)
            # print_linked_list(l2)
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
# @lc code=end

if __name__ == '__main__':
    l = Solution().mergeTwoLists(construct_linked_list([1,2,4]), construct_linked_list([1,3,4]))
    print_linked_list(l)
