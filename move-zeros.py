class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numlen = len(nums)
        p = 0
        for i in range(numlen):
            if nums[i]==0:
                p+=1
        j=0
        for i in range(numlen):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for i in range(p):
            nums[i+numlen-p]=0