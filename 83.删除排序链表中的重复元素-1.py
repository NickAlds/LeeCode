# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。 
# 
#  示例 1: 
# 
#  输入: 1->1->2
# 输出: 1->2
#  
# 
#  示例 2: 
# 
#  输入: 1->1->2->3->3
# 输出: 1->2->3 
#  Related Topics 链表 
#  👍 452 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode("", next=head)
        pre, cur = dummy.next, dummy.next.next
        while pre and cur:
            if pre.val != cur.val:
                pre, cur = pre.next, cur.next
                continue
            while cur.next and pre.val == cur.next.val:
                cur = cur.next
            pre.next = cur.next
            cur = cur.next
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
