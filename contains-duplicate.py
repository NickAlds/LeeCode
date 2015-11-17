class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numdict = {}
        for i in nums:
            if numdict.has_key(i):
                return True
            else :
                numdict[i] = 1
        return False