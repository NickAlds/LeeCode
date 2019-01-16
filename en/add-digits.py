class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numdigits = str(num)
        while(len(numdigits) > 1):
        	sum = 0
        	for i in numdigits:
        		sum+=int(i)
        	numdigits = str(sum)
        return int(numdigits)