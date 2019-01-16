'''
230. Kth Smallest Element in a BST
Description  Submission  Solutions
Total Accepted: 86901
Total Submissions: 204148
Difficulty: Medium
Contributors: Admin
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cache = []
        def inorderbst(root):
            if root:
                inorderbst(root.left)
                cache.append(root.val)
                if len(cache) == k:
                    return cache.pop()
                inorderbst(root.right)
        return inorderbst(0)

