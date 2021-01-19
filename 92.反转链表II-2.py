# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。 
# 
#  说明: 
# 1 ≤ m ≤ n ≤ 链表长度。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL 
#  Related Topics 链表 
#  👍 644 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(next=head)
        nodes = []
        pre, cur = dummy, dummy.next
        cnt = 1
        while cur and cnt <= n:
            if cnt < m:
                pre, cur = pre.next, cur.next
            else:
                nodes.append(cur)
                cur = cur.next
            cnt += 1
        nodes.reverse()
        # print([i.val for i in nodes])
        pre.next = nodes[0]
        nodes[-1].next = nodes[0].next
        # print_linked_list(nodes[-1])
        for i in range(1, n-m+1):
            print(nodes[i].val)
            nodes[i-1].next = nodes[i]
        return dummy.next

    def reverse_all(self, head):
        if not head.next:
            return head
        last = self.reverse_all(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseN(self, head, n):
        if n == 1:
            return head, head.next
        last, successor = self.reverseN(head.next, n-1)
        # successor = head.next.next
        head.next.next = head
        head.next = successor
        return last, successor

    def reverseMN(self, head, m, n):
        if m == 1:
            return self.reverseN(head, n)[0]
        head.next = self.reverseMN(head.next, m-1, n-1)
        return head

