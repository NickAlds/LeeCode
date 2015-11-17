class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nlen = len(nums)
        res = [0]*nlen
        res[0] = 1
        for i in range(1,nlen):
            res[i] = res[i-1]*nums[i-1]
        rearproduct = 1
        for i in range(nlen):
            res[nlen-1-i] = res[nlen-1-i] * rearproduct
            rearproduct*=nums[nlen-1-i]
        return res
