'''
398. Random Pick Index
Description  Submission  Solutions
Total Accepted: 15508
Total Submissions: 37586
Difficulty: Medium
Contributors: Admin
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
Subscribe to see which companies asked this question.
'''
import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        pool = []
        lenpool = 0
        for index, num in enumerate(self.nums):
            if num == target:
                rand = random.randrange(lenpool+1)
                if rand == lenpool:
                    pick = index
                else:
                    pick = pool[rand]
                pool.append(index)
                lenpool += 1
        return pick
