'''
167. Two Sum II - Input array is sorted
Description  Submission  Solutions  Add to List
Total Accepted: 53889
Total Submissions: 111957
Difficulty: Easy
Contributors: Admin
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers)
        while True:
            mid = (start + end)/2
            if numbers[mid]+numbers[0] > target:
                end = mid
            elif end == mid+1 or (end > mid + 1 and numbers[mid+1]+numbers[0] > target):
                pt = mid
                break
            else:
                start = mid
        while pt > 0:
            for i in range(pt+1):
                if numbers[i] + numbers[pt] > target:
                    break
                elif numbers[i] + numbers[pt] == target:
                    return [i+1, pt+1]
            pt -= 1


s1 = Solution()
numbers1, target = [2, 7, 11, 15], 9

print s1.twoSum(numbers1, target)
