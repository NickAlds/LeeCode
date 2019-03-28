#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (43.06%)
# Total Accepted:    486.9K
# Total Submissions: 1.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution:
    def maxSubArray1(self, nums: List[int]):
        maxi = nums[0]
        cur = 0
        for i in nums:
            if cur < 0:
                cur = i
            else:
                cur += i
            if cur > maxi:
                maxi = cur
        return maxi
    def maxSubArray(self, nums: List[int]):
        return self.divide(nums, 0, len(nums)-1)
    def divide(self, nums, left, right):
        if left==right:
            return nums[left]
        mid = (left+right)//2
        left_max = self.divide(nums, left, mid)
        right_max = self.divide(nums, mid+1, right)
        left_part_cur = right_part_cur = 0
        left_part_max = nums[mid]
        right_part_max = nums[mid+1]
        for i in range(mid, left-1, -1):
            left_part_cur += nums[i]
            if left_part_cur > left_part_max:
                left_part_max = left_part_cur
        for i in range(mid+1, right+1,):
            right_part_cur += nums[i]
            if right_part_cur > right_part_max:
                right_part_max = right_part_cur
        return max(left_max, right_max, left_part_max+right_part_max)
