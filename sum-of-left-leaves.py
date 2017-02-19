# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.calculate_sum(root, 0)
    def calculate_sum(self, root, flag):
        if not root:
            return 0
        if not root.left and not root.right:
            if flag:
                return root.val
            else:
                return 0
        elif root.left and not root.right:
            return self.calculate_sum(root.left, 1)
        elif not root.left and root.right:
            return self.calculate_sum(root.right, 0)
        else:
            return self.calculate_sum(root.left, 1) + self.calculate_sum(root.right, 0)

root = TreeNode(3)
node1 = TreeNode(20)
root.left = TreeNode(9)
node1.left = TreeNode(15)
node1.right = TreeNode(7)
root.right = node1

s1 = Solution()
print s1.sumOfLeftLeaves(root)
print s1.sumOfLeftLeaves(node1)
