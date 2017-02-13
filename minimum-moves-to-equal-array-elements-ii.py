class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mindex = len(nums)/2
        sum = 0
        for i in nums:
            sum += abs(i - nums[mindex])
        return sum
