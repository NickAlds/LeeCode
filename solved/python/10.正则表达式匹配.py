#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    # 右到左查看是否匹配会遗漏一些case 如"aaa" "ab*a*c*a"
    # 因为右到左不是最小子问题
    def isMatch1(self, s: str, p: str) -> bool:
        print(s,p)
        if not s and not p:
            return True
        lens, lenp = len(s), len(p)
        if not p:
            return False
        elif not s:
            if p[-1] == "*" and lenp>1:
                return self.isMatch1(s, p[:lenp-2])
            else:
                return False
        i, j = lens-1, lenp -1
        if s[i] == p[j] or p[j] == ".":
            return self.isMatch1(s[:i], p[:j])
        elif p[j] == "*" and j > 0:
            while i >= 0 and (p[j-1] == s[i] or p[j-1] == "."):
                i -= 1
            return self.isMatch1(s[:i+1], p[:j-1])
        else:
            return False

    # 从左到右匹配
    def isMatch(self, s: str, p: str) -> bool:
        # s[:i] 和 p[:j]的尾部是否匹配
        def matches(i: int, j: int) -> bool:
            if i == 0:  # 尾部肯定不匹配
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] |= dp[i][j-2]
                    if matches(i, j-1):
                        dp[i][j] |= dp[i-1][j]
                    else:
                        dp[i][j] |= dp[i][j-2]
                else:
                    if matches(i, j):
                        dp[i][j] |= dp[i-1][j-1]

        return dp[m][n]


            
# @lc code=end
if __name__ == '__main__':
    print(Solution().isMatch("aaa", "ab*a*c*a"))
