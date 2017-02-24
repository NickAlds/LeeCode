'''
350. Intersection of Two Arrays II
Description  Submission  Solutions
Total Accepted: 53305
Total Submissions: 121621
Difficulty: Easy
Contributors: Admin
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1, dict2 = {}, {}
        for i in nums1:
            if dict1.has_key(i):
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in nums2:
            if dict2.has_key(i):
                dict2[i] += 1
            else:
                dict2[i] = 1
        res = []
        for i in dict1:
            if dict2.has_key(i):
                res += [i]*min(dict1[i], dict2[i])
        return res
