class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in s:
            sum = sum*26 + ord(i)-ord('A')+1
        return sum
