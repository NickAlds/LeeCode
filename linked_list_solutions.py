from lc_types import ListNode, construct_linked_list, print_linked_list,\
    TreeNode, print_tree
from typing import List


class Solution:
    def deleteDuplicatesii(self, head: ListNode) -> ListNode:
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

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        def constructBST(nums):
            n = len(nums)
            if not nums:
                return None
            root = TreeNode(val=nums[n//2])
            if n == 1:
                return root
            root.left = constructBST(nums[:n//2])
            root.right = constructBST(nums[n//2+1:])
            return root
        return constructBST(vals)


if __name__ == '__main__':
    # print_linked_list(Solution().reverseMN(construct_linked_list([1, 2, 3, 4, 5, 6]), 2,4))
    print_tree(Solution().sortedListToBST(construct_linked_list([1,2,3,4,5,6,7])))


