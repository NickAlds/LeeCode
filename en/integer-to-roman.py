'''
12. Integer to Roman
Description  Submission  Solutions
Total Accepted: 94950
Total Submissions: 219363
Difficulty: Medium
Contributors: Admin
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #IXCM VLD
        res = ''
        res += num/1000 * 'M'
        num %= 1000
        if num >= 900:
            res += 'CM'
        elif num >= 500:
            res += 'D' + (num%500/100)*'C'
        elif num >= 400:
            res += 'CD'
        elif num >= 100:
            res += 'C'*(num/100)
        num %= 100
        if num >= 90:
            res += 'XC'
        elif num >= 50:
            res += 'L' + (num%50/10)*'X'
        elif num >= 40:
            res += 'XL'
        elif num >= 10:
            res += 'X'*(num/10)
        num %= 10
        if num == 9:
            res += 'IX'
        elif num >= 5:
            res += 'V' + num%5*'I'
        elif num == 4:
            res += 'IV'
        elif num >= 1:
            res += 'I'*num
        return res
