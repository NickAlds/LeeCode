#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (69.10%)
# Total Accepted:    18K
# Total Submissions: 26.1K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 
# 例如，给出 n = 3，生成结果为：
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
# 
#

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(res, n, s, left, right) :
            if right == n : res.append(s)
            if left < n :
                dfs(res, n, s + "(", left+1, right)
            if left > right :
                dfs(res, n, s + ")", left, right+1)
        dfs(res, n, '', 0, 0)
        return res


