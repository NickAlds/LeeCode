#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (22.94%)
# Total Accepted:    457.4K
# Total Submissions: 2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution1:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rst, length = [], len(nums)
        for index, num in enumerate(nums):
            left, right = index+1, length-1
            while left < right:
                sum3 = nums[left]+nums[right]+num
                if sum3 < 0:
                    left += 1
                elif sum3 >0 :
                    right -=1
                else:
                    if [num, nums[left], nums[right]] not in rst:
                        rst.append([num, nums[left], nums[right]])
                    left += 1
        return rst
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #from collections import defaultdict
        from bisect import bisect_left, bisect_right
       
        target = 0
        
        result = []
        length = len(nums)
        
        if length < 3:
            return result
        
        count ={}
        # map the counts
        for n in nums:
            count[n] = count.get(n, 0)+1
            
        keys = list(count.keys())
        keys.sort()
      
        t3 = target // 3
        if t3 in keys and count[t3] >= 3:
            result.append([t3, t3, t3])

        begin = bisect_left(keys, target - keys[-1] * 2)
        end = bisect_left(keys, target * 3)

        for i in range(begin, end):
            a = keys[i]
            if count[a] >= 2 and target - 2 * a in count:
                result.append([a, a, target - 2 * a])

            max_b = (target - a) // 2  # target-a is remaining
            min_b = target - a - keys[-1]  # target-a is remaining and c can max be keys[-1]
            b_begin = max(i + 1, bisect_left(keys, min_b))
            b_end = bisect_right(keys, max_b)

            for j in range(b_begin, b_end):
                b = keys[j]
                c = target - a - b
                if c in count and b <= c:
                    if b < c or count[b] >= 2:
                        result.append([a, b, c])
        return result
# s = Solution()
# print(s.threeSum([-1,0,1,2,-1,-4]))
