'''
343. Integer Break
Description  Submission  Solutions
Total Accepted: 36507
Total Submissions: 80883
Difficulty: Medium
Contributors: Admin
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Show Hint 
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.
'''
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        cnt2 = 0
        if n%3:
            cnt2 = 3 - n%3
        cnt3 = (n-2*cnt2)/3
        return 3**cnt3 * 2**cnt2