#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        cur = 0
        ans = 0
        n = len(s)
        while n > 0:
            if cur <= table[s[n-1]]:
                ans += table[s[n-1]]
                cur = table[s[n-1]]
            else:
                ans -= table[s[n-1]]
            n -= 1
        return ans

# @lc code=end
if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
