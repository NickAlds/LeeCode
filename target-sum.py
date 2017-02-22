'''
494. Target Sum Add to List
Description  Submission  Solutions
Total Accepted: 8891
Total Submissions: 19997
Difficulty: Medium
Contributors: kevin.xinzhao@gmail.com
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dictw = {}
        def way_num(index, target):
            if dictw.has_key((index, target)):
                return dictw[(index, target)]
            if index == len(nums):
                r = 0+bool(not target)
                dictw[(index, target)] = r
                return r
            r = way_num(index+1, target+nums[index]) + way_num(index+1, target-nums[index])
            dictw[(index, target)] = r
            return r
        return way_num(0, S)
print Solution().findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0)