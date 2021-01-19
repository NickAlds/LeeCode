#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List
# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        min_diff = 3001
        ans = 0
        nums.sort()
        for a in range(n):
            if a > 0 and nums[a-1]==nums[a]:
                continue
            b, c = a+1, n-1
            while b < c:
                diff = nums[a]+nums[b]+nums[c]-target
                # print([a, b, c, nums[a], nums[b], nums[c]])
                if diff > 0:
                    c -= 1
                    if diff < min_diff:
                        ans = diff + target
                        min_diff = diff
                elif diff < 0:
                    b += 1
                    if -1*diff < min_diff:
                        ans = diff + target
                        min_diff = -1*diff
                else:
                    return target
        return ans
# @lc code=end
if __name__ == '__main__':
    print(Solution().threeSumClosest([0,2,1,-3], 1))
