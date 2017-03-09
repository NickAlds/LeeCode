'''
312. Burst Balloons
Description  Submission  Solutions
Total Accepted: 23001
Total Submissions: 54845
Difficulty: Hard
Contributors: Admin
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        coins = [1] + [num for num in nums if num] + [1]
        n = len(coins)
        dp = [[0] * n for _ in xrange(n)]

        for l in xrange(2, n):
            for left in xrange(0, n-l):
                right = left + l
                for j in xrange(left+1, right):
                    dp[left][right] = max(dp[left][right], dp[left][j] + \
                            dp[j][right] + coins[left] * coins[j] * coins[right])
        print dp
        return dp[0][n-1]
print Solution().maxCoins([3,1,5,8])