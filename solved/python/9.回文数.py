#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        before, after = x, 0
        while x:
            after = 10*after + x%10
            x//=10
        return before == after
# @lc code=end
print(Solution().isPalindrome(1211))
