#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (27.34%)
# Total Accepted:    298.9K
# Total Submissions: 1.1M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
#
class Solution1:
    def myPow(self, x: float, n: int):
        return x**n

class Solution2:
    def myPow(self, x: float, n: int):
        if n==0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        elif n%2:
            return self.myPow(x*x, n//2)*x
        else:
            return self.myPow(x*x, n//2)

class Solution:
    def myPow(self, x: float, n: int):
        if n==0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        pow = 1
        while n:
            if n%2:
                pow *= x
            x = x*x
            n = n//2
        return pow
        