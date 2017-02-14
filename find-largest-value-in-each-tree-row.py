'''
515. Find Largest Value in Each Tree Row
Description  Submission  Solutions  Add to List
Total Accepted: 1909
Total Submissions: 3759
Difficulty: Medium
Contributors: love_FDU_llp
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxlst = [root.val]
        self.nodedepth(root, 0, maxlst)
        return maxlst
    def nodedepth(self, node, depth, maxlst):
        if not node.left and not node.right:
            return maxlst
        elif not node.left:
            if len(maxlst)-1 > depth:
                maxlst[depth+1] = max(maxlst[depth+1], node.right.val)
            else:
                maxlst.append(node.right.val)
            self.nodedepth(node.right, depth+1, maxlst)
        elif not node.right:
            if len(maxlst)-1 > depth:
                maxlst[depth+1] = max(maxlst[depth+1], node.left.val)
            else:
                maxlst.append(node.left.val)
            self.nodedepth(node.right, depth+1, maxlst)
        else:
            if len(maxlst)-1 > depth:
                maxlst[depth+1] = max(maxlst[depth+1], node.left.val, node.right.val)
            else:
                maxlst.append(max(node.left.val, node.right.val))
            self.nodedepth(node.right, depth+1, maxlst)
            self.nodedepth(node.left, depth+1, maxlst)

