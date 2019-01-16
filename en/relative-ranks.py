'''
506. Relative Ranks
Description  Submission  Solutions  Add to List
Total Accepted: 3565
Total Submissions: 7038
Difficulty: Easy
Contributors: taylorty
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
Subscribe to see which companies asked this question.
'''
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        length = len(nums)
        ndict = {}
        nums1 = [0]*length
        for i, num in enumerate(nums):
            ndict[num] = i
        nums.sort()

        for i, num in enumerate(nums):
            if i == length-1:
                nums1[ndict[num]] = "Gold Medal"
            elif i == length-2:
                nums1[ndict[num]] = "Silver Medal"
            elif i == length-3:
                nums1[ndict[num]] = "Bronze Medal"
            else:
                nums1[ndict[num]] = str(length-i)
        return nums1
