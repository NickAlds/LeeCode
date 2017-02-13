class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        length = len(nums)
        ndict = {}
        nums1 = [0]*length
        for i, num in enumerate(nums):
            ndict[num] = i
        nums.sort()

        for i, num in enumerate(nums):
            if i == length-1:
                nums1[ndict[num]] = "Gold Medal"
            elif i == length-2:
                nums1[ndict[num]] = "Silver Medal"
            elif i == length-3:
                nums1[ndict[num]] = "Bronze Medal"
            else:
                nums1[ndict[num]] = str(length-i)
        return nums1
