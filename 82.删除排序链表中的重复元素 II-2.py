# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#  
# 
#  示例 2: 
# 
#  输入: 1->1->1->2->3
# 输出: 2->3 
#  Related Topics 链表 
#  👍 433 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lc_types import ListNode, construct_linked_list, print_linked_list
from typing import List
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode("", next=head)
        prepre, pre, cur = dummy, dummy.next, dummy.next.next
        while pre and cur:
            if pre.val != cur.val:
                prepre, pre, cur = prepre.next, pre.next, cur.next
                continue
            while cur.next and pre.val == cur.next.val:
                cur = cur.next
            prepre.next = cur.next
            pre = cur.next if cur.next else None
            cur = pre.next if pre else None
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
