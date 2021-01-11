#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
from typing import List


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for _ in range(n - k % n):
            nums.append(nums.pop(0))
# @lc code=end

