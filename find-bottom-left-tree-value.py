'''
513. Find Bottom Left Tree Value
Description  Submission  Solutions  Add to List
Total Accepted: 2100
Total Submissions: 4185
Difficulty: Medium
Contributors: abhijeet17
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxlst = [root.val]
        self.nodedepth(root, 0, maxlst)
        return maxlst[-1]
    def nodedepth(self, node, depth, maxlst):
        if not node.left and not node.right:
            return
        elif not node.left:
            if len(maxlst) < depth+2:
                maxlst.append(node.right.val)
            self.nodedepth(node.right, depth+1, maxlst)
        elif not node.right:
            if len(maxlst) < depth+2:
                maxlst.append(node.left.val)
            self.nodedepth(node.left, depth+1, maxlst)
        else:
            if len(maxlst) < depth+2:
                maxlst.append(node.left.val)
            self.nodedepth(node.left, depth+1, maxlst)
            self.nodedepth(node.right, depth+1, maxlst)