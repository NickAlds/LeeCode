'''
508. Most Frequent Subtree Sum
Description  Submission  Solutions  Add to List
Total Accepted: 2731
Total Submissions: 5251
Difficulty: Medium
Contributors: Cyber233
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

Subscribe to see which companies asked this question.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sumdict = {}
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        sumdict = {'max':0}
        self.nodesum(root, sumdict)
        sumlist = []
        for key in sumdict.keys():
            if key != 'max' and sumdict[key] == sumdict['max']:
                sumlist.append(key)
        return sumlist
    def nodesum(self, node, sumdict):
        if not node.left and not node.right:
            self.dictadd(sumdict, node.val)
            return node.val
        elif not node.left:
            sbtsum = node.val + self.nodesum(node.right, sumdict)
            self.dictadd(sumdict, sbtsum)
            return sbtsum
        elif not node.right:
            sbtsum = node.val + self.nodesum(node.left, sumdict)
            self.dictadd(sumdict, sbtsum)
            return sbtsum
        else:
            sbtsum = node.val + self.nodesum(node.left, sumdict) + self.nodesum(node.right, sumdict)
            self.dictadd(sumdict, sbtsum)
            return sbtsum
    def dictadd(self, dict1, a):
        if dict1.has_key(a):
            dict1[a] += 1
        else:
            dict1[a] = 1
        dict1['max'] = max(dict1[a], dict1['max'])
