class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {"max":-1}
        for i in nums:
            if dict.has_key(i):
                dict[i]+=1
            else:
                dict[i]=1
            if dict[i]>dict["max"]:
                dict["max"] = dict[i]
                dict["maxnum"] = i
        if dict["max"]>=len(num)/2:
            return dict["maxnum"]
        return dict["maxnum"]
