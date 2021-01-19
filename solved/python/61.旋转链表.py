# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#  
# 
#  示例 2: 
# 
#  输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL 
#  Related Topics 链表 双指针 
#  👍 395 👎 0

from lc_types import ListNode, print_linked_list, construct_linked_list

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0, next=head)
        l = 0
        while head:
            head = head.next
            l += 1
        k = k % l
        slow = fast = dummy
        for _ in range(k):
            fast = fast.next
        while fast.next and slow.next:
            fast = fast.next
            slow = slow.next
        # if slow is dummy:
        #     return head
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next

if __name__ == '__main__':
    print_linked_list(Solution().rotateRight(construct_linked_list([1,2,3,4]), 2000000))


# leetcode submit region end(Prohibit modification and deletion)
