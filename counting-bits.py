class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        slist = [0] * (num+1)
        for i in range(1, num+1):
            slist[i] = slist[i >> 1] + i % 2
        return slist
