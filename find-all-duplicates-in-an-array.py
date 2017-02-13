'''
442. Find All Duplicates in an Array
Description  Submission  Solutions  Add to List
Total Accepted: 15704
Total Submissions: 30719
Difficulty: Medium
Contributors: shen5630
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
Subscribe to see which companies asked this question.
'''
#The idea is we do a linear pass using the input array itself as a hash to store which numbers have been seen before. We do this by making elements at certain indexes negative. See the full explanation here
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplist = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                duplist.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return duplist
