"""
540. Single Element in a Sorted Array
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numlen = len(nums)
        mid = numlen/2
        while mid > 0 and mid < numlen-1:
            if nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            if mid%2 == (nums[mid] == nums[mid-1]):
                mid = (mid+numlen)/2
            else:
                mid /= 2
        return nums[mid]
    def singleNonDuplicate1(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
nums = [3,3,7,7,10,11,11]
print Solution().singleNonDuplicate(nums)

        