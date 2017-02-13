class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mid = int(area**0.5)
        while mid > 0:
            if area%mid == 0:
                return [area/mid, mid]
            mid -= 1

s1 = Solution()
i = 9999993

print s1.constructRectangle(i)