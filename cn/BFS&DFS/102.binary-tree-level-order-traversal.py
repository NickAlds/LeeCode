#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (47.48%)
# Total Accepted:    352.2K
# Total Submissions: 740.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        array, queue = [], [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            array += [(node, level)]
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        res = []
        for node, level in array:
            if level == len(res):
                res.append([])
            res[level].append(node.val)
        return res

