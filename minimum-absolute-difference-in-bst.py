'''
530. Minimum Absolute Difference in BST
Description  Submission  Solutions
Total Accepted: 2251
Total Submissions: 4623
Difficulty: Easy
Contributors: nagasupreeth
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mini = [0xFFFFFFFF]
        cache = [-0xFFFFFFFF]
        self.in_order(root, mini, cache)
        return mini[0]
    def in_order(self, root, mini, cache):
        if root:
            self.in_order(root.left, mini, cache)
            mini[0] = min(mini[0], root.val - cache[0])
            cache[0] = root.val
            self.in_order(root.right, mini, cache)

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        srt = []
        self.in_order(root, srt)
        MIN = 0xFFFFFFFF
        for i in xrange(len(srt)-1):
            MIN = min(srt[i+1]-srt[i], MIN)
        return MIN
    def in_order(self, root, srt):
        if root:
            self.in_order(root.left, srt)
            srt.append(root.val)
            self.in_order(root.right, srt)


