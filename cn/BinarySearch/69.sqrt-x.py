#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (31.04%)
# Total Accepted:    353.5K
# Total Submissions: 1.1M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution:
    def mySqrt(self, x: int):
        if x in [0, 1]:
            return x
        cur = x
        while True:
            if cur**2==x:
                return cur
            elif (cur//2)**2 < x:
                break
            cur//=2
        l, r = cur//2, cur
        while r > l:
            mid = (r+l)//2
            if mid**2==x or mid**2<x<(mid+1)**2:
                return mid
            elif mid**2 > x:
                r = mid
            else:
                l = mid    
        return l
    def mySqrt1(self, x):
        return int(x**0.5)
print(Solution().mySqrt(6))
