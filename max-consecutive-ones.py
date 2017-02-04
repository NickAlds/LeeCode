"""
485. Max Consecutive Ones
Description  Submission  Discussion  Add to List
Total Accepted: 14278
Total Submissions: 25362
Difficulty: Easy
Contributors: Stomach_ache
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = -1
        max = 0
        length = len(nums)
        for i in range(length):
            if (not i or not nums[i-1]) and nums[i]:
                start = i
            if (i==length-1 and nums[i]) or (i<length-1 and nums[i] and not nums[i+1]):
                end = i
                if end - start >= max:
                    max = end - start + 1
        return max
class BetterSolution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans

s = Solution()
nums = [1]

print s.findMaxConsecutiveOnes(nums)
