class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numdict = {}
        for num in nums:
            if num in numdict:
                numdict[num]+=1
            else:
                numdict[num]=1
        for i in numdict.keys():
            if numdict[i]==1:
                return i
