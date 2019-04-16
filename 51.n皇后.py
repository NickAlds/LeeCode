#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (60.30%)
# Total Accepted:    5.8K
# Total Submissions: 9.6K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 示例:
# 
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
#
class Solution:
    def solveNQueens1(self, n: int):
        self.paths = []
        self.dfs(n, 0, set(), set(), set(), [])
        
        return [['.'*i+'Q'+'.'*(n-1-i)  for i in path]
                    for path in self.paths]
    
    def dfs(self, n, level, set_x, set_xpy, set_xmy, cur):
        if level >= n:
            self.paths.append(cur)
            return
        for i in range(n):
            if i in set_x or i+level in set_xpy or i-level in set_xmy:
                continue
            self.dfs(n, level+1, set_x|{i}, set_xpy|{i+level}, set_xmy|{i-level}, cur+[i])
print([Solution().solveNQueens(i) for i in range(10)])
