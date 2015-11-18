root# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    preorder = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root != None:
            preorder.append(root.val)
            preorderTraversal(root.left)
            preorderTraversal(root.right)
        return preorder