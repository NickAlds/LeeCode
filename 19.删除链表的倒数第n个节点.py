#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 记录长度
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        queue = []
        start = ListNode(next=head)
        while start:
            queue.append(start)
            if len(queue) > n+1:
                queue.pop(0)
                continue
        queue[0].next = queue[1].next
        return head

    # 快慢指针
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
# @lc code=end

