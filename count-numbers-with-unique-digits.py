'''
357. Count Numbers with Unique Digits
Description  Submission  Solutions
Total Accepted: 27796
Total Submissions: 61357
Difficulty: Medium
Contributors: Admin
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

Hint:

A direct way is to use the backtracking approach.
'''
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 1
        if n == 1:
            return 10
        cntn, i = 9, 1
        while i < n and i < 10:
            cntn *= 9-i+1
            i += 1
        return cntn + self.countNumbersWithUniqueDigits(n-1)
