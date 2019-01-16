'''
496. Next Greater Element I
Description  Submission  Solutions  Add to List
Total Accepted: 3176
Total Submissions: 5284
Difficulty: Easy
Contributors: love_FDU_llp
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
'''

#O(m*n) Solution
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        length = len(nums)
        for i in findNums:
            j, flag = 0, False
            while j < length:
                if i == nums[j] and not flag:
                    temp = nums[j]
                    flag = True
                if flag:
                    if j < length-1 and nums[j+1] > i:
                        res.append(nums[j+1])
                        flag = False
                        break
                if j == length - 1:
                    res.append(-1)
                    flag = False
                j += 1
        return res

#O(m+n) Solution#
class Solution1(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        ans = [-1] * len(findNums)
        for i, num in enumerate(findNums):
            d[num] = i
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                top = stack.pop()
                if top in d:
                    ans[d[top]] = num
            stack.append(num)
        return ans
s1 = Solution()
findNums, nums = [1,3,5,2,4], [6,5,4,3,2,1,7]
print s1.nextGreaterElement(findNums,nums)