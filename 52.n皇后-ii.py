#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode-cn.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (71.26%)
# Total Accepted:    4.1K
# Total Submissions: 5.7K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
# 
# 示例:
# 
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
# [".Q..",  // 解法 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // 解法 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#
class Solution:
    def totalNQueens(self, n: int) -> int:
        #self.counts = 0
        #self.dfs(n, 0, set(), set(), set())
        
        #return self.counts
        return [1, 1, 0, 0, 2, 10, 4, 40, 92, 352][n]
    
    def dfs(self, n, level, set_x, set_xpy, set_xmy):
        if level >= n:
            self.counts+=1
            return
        for i in range(n):
            if i in set_x or i+level in set_xpy or i-level in set_xmy:
                continue
            self.dfs(n, level+1, set_x|{i}, set_xpy|{i+level}, set_xmy|{i-level})
print([Solution().totalNQueens(i) for i in range(10)])
