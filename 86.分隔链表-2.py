# 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。 
# 
#  你应当保留两个分区中每个节点的初始相对位置。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：head = 1->4->3->2->5->2, x = 3
# 输出：1->2->2->4->3->5
#  
#  Related Topics 链表 双指针 
#  👍 354 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        pre_tail = None
        while cur:
            if not pre_tail:
                if cur.val >= x:
                    pre_tail = pre
                pre, cur = pre.next, cur.next
            else:
                if cur.val < x:
                    pre.next = cur.next
                    cur.next = pre_tail.next
                    pre_tail.next = cur
                    cur = pre.next
                    pre_tail = pre_tail.next
                else:
                    pre, cur = pre.next, cur.next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
