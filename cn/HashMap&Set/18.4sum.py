#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (29.32%)
# Total Accepted:    204.1K
# Total Submissions: 695.9K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import itertools
        res = []
        nums.sort()
        if len(nums)<4 or sum(nums[:4]) > target:
            return res
        for i, num in enumerate(nums):
            tmp_target = target - num
            tri_nums = nums[i+1:]
            tri_res = self.threeSum(tri_nums, tmp_target)
            #print(tri_res, target, num, tmp_target)
            res += [[num]+r for r in tri_res]
        res.sort()
        return list(ans for ans,_ in itertools.groupby(res))
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst, length = [], len(nums)
        for index, num in enumerate(nums):
            left, right = index+1, length-1
            while left < right:
                sum3 = nums[left]+nums[right]+num
                if sum3 < target:
                    left += 1
                elif sum3 >target :
                    right -=1
                else:
                    if [num, nums[left], nums[right]] not in rst:
                        rst.append([num, nums[left], nums[right]])
                    left += 1
        return rst

s = Solution()
a = s.fourSum([1,-2,-5,-4,-3,3,3,5], -11)
print(a)

