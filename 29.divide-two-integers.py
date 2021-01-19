#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        pos = True
        if divisor > 0:
            pos = not pos
            divisor = 0-divisor
        if dividend > 0:
            pos = not pos
            dividend = 0-dividend
        if divisor < dividend:
            return 0
        res, mul_divisor = 1, divisor
        while dividend < mul_divisor+mul_divisor:
            res += res
            mul_divisor += mul_divisor
        res += self.divide(dividend-mul_divisor, divisor)
        if not pos:
            res = 0-res
        if res < -2147483648:
            res = -2147483648
        if res > 2147483647:
            res = 2147483647
        return res

# @lc code=end
if __name__ == '__main__':
    print(Solution().divide(-1, 1))
