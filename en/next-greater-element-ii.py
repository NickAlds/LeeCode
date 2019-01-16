'''
503. Next Greater Element II
Description  Submission  Solutions
Total Accepted: 3334
Total Submissions: 7237
Difficulty: Medium
Contributors: love_FDU_llp
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
'''
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        length = len(nums)
        res = [-1]*length
        i = 0
        while i < 2*length:
            while stack and stack[-1][1] < nums[i%length]:
                index, top = stack.pop()
                res[index] = nums[i%length]
            stack.append((i%length, nums[i%length]))
            i += 1
        return res

s1 = Solution()
test = [1, 2, 1]

print s1.nextGreaterElements(test)

