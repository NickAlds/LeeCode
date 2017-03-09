'''
415. Add Strings
Description  Submission  Solutions
Total Accepted: 25637
Total Submissions: 62216
Difficulty: Easy
Contributors: Admin
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        maxl = -1
        if l1 > l2:
            num2 = '0'*(l1-l2)+num2
            maxl = l1
        else:
            num1 = '0'*(l2-l1)+num2
            maxl = l2
        print maxl, num1, num2
        next1 = 0
        summ = ''
        for i in xrange(maxl-1, -1, -1):
            tmp = int(num1[i])+int(num2[i])+next1
            summ = str(tmp%10) + summ
            next1 = tmp/10
        if next1:
            return '1'+summ
        else:
            return summ

print Solution().addStrings('989189', '12222')
        