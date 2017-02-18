'''
504. Base 7 Add to List
Description  Submission  Solutions
Total Accepted: 4053
Total Submissions: 8710
Difficulty: Easy
Contributors: satyapriya
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return 0
        absnum = abs(num)
        sevenbasenum = ""
        while absnum > 0:
            absnum, x = absnum/7, absnum%7
            sevenbasenum = str(x) + sevenbasenum
        if num < 0:
            sevenbasenum = '-'+sevenbasenum
        return sevenbasenum
