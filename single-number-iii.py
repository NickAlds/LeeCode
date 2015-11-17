class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numdict = {}
        singlenums = []
        for i in nums:
            if numdict.has_key(i):
                numdict[i]+=1
            else:
                numdict[i]=1
        for i in numdict.keys():
            if numdict[i]==1:
                singlenums.append(i)
        return singlenums

