"""
637. Average of Levels in Binary Tree
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        sums = []
        def dfs(root, depth):
            if root:
                if depth >= len(sums):
                    sums.append([0,0])
                sums[depth][0] += 1
                sums[depth][1] += root.val
                dfs(root.left,depth+1)
                dfs(root.right, depth+1)
        if root:
            dfs(root, 0)
        return [i[1]*1.0/i[0] for i in sums]
s1 = Solution()
node = TreeNode(5)
node.left = TreeNode(2)
node.right = TreeNode(-3)
print s1.averageOfLevels(node)
