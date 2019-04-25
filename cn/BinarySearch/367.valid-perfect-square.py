#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.60%)
# Total Accepted:    106K
# Total Submissions: 267.5K
# Testcase Enumample:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Enumample 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Enumample 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#
class Solution:
    def isPerfectSquare(self, num: int):
        if num in [0, 1]:
            return True
        cur = num
        while True:
            if cur**2==num:
                return True
            elif (cur//2)**2 < num:
                break
            cur//=2
        l, r = cur//2, cur
        while r > l:
            mid = (r+l)//2
            if mid**2==num:
                return True
            if mid**2<num<(mid+1)**2:
                return False
            if mid**2 > num:
                r = mid
            else:
                l = mid
        

