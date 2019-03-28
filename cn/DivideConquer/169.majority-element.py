#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (51.84%)
# Total Accepted:    359.2K
# Total Submissions: 692.9K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#


class Solution1:
    def majorityElement(self, nums):
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]


class Solution2:
    def majorityElement(self, nums):
        return sorted(nums)[len(nums)//2]


class Solution:
    def majorityElement(self, nums):
        l = len(nums)
        if l == 1:
            return nums[0]
        #print(nums, nums[:l//2], nums[l//2:])
        left = self.majorityElement(nums[:l//2])
        right = self.majorityElement(nums[l//2:])
        if left == right:
            return left
        else:
            if nums.count(left) > nums.count(right):
                return left
            else:
                return right
