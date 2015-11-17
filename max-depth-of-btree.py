# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    result = -1
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        self.helper(root,1)
        return self.result
    def helper(self,root,depth):
        if root.left==None and root.left == None:
            self.result = max(self.result,depth)
        if root.left:
            self.helper(root.left,depth+1)
        if root.right:
            self.helper(root.right,depth+1)