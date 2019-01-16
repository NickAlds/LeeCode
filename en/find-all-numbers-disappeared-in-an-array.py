'''
448. Find All Numbers Disappeared in an Array
Description  Submission  Solutions  Add to List
Total Accepted: 24919
Total Submissions: 46356
Difficulty: Easy
Contributors: yuhaowang001
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            index = abs(i) - 1
            nums[index] = -abs(i)
            return [i+1 for i in range(len(nums)) if nums[i]>0]