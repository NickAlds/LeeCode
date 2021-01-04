#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    # 暴力dp 超时了
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        ans = []
        # 枚举子串长度 l+1
        for l in range(n):
            for i in range(n):
                j = i+l
                if j > n - 1:
                    break
                if l == 0:
                    dp[i][j] = 1
                elif l == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and j-i+1 > len(ans):
                    ans = s[i:j+1]
        return ans

    @staticmethod
    def maxSeqLength(s, l, r):
        while l>-1 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return l+1, r-1

    # 最小情形拓展到最大
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = end = 0

        for i in range(len(s)):
            l1, r1 = self.maxSeqLength(s, i, i)
            l2, r2 = self.maxSeqLength(s, i, i+1)
            if end - start < r1 - l1:
                start, end = l1, r1
            if end - start < r2 - l2:
                start, end = l2, r2
        return s[start: end+1]

        
# @lc code=end

