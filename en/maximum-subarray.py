'''
53. Maximum Subarray
Description  Submission  Solutions
Total Accepted: 174235
Total Submissions: 446513
Difficulty: Easy
Contributors: Admin
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

Subscribe to see which companies asked this question.

Show Tags
Show Similar Problems
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = 0
        ans = -0xFFFFFFFF
        for i in nums:
            summ += i
            ans = max(summ, ans)
            if summ < 0:
                summ = 0
        return ans
