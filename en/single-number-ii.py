'''
137. Single Number II
Description
Total Accepted: 108821
Total Submissions: 269134
Difficulty: Medium
Contributors: Admin
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumlist = [0]*32
        summary, negcnt = 0, 0
        for i in nums:
            negcnt += i < 0
            i = abs(i)
            bitwise = format(i, '032b')
            for j in xrange(32):
                sumlist[j] += int(bitwise[j])
        for i in xrange(32):
            summary += 2**(31-i)*(sumlist[i]%3)
        return summary*[1,-1][negcnt%3]
