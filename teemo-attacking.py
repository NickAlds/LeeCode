class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        if len(timeSeries) == 0:
            return 0
        for i in range(len(timeSeries)-1):
            total += min(timeSeries[i+1]-timeSeries[i], duration)
        return total+duration

s1 = Solution()
timeSeries, duration = [1,4], 2
print s1.findPoisonedDuration(timeSeries, duration)