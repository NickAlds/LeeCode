#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    # 3指针 ab往右 c往左
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        ans = []
        nums.sort()
        for a in range(n):
            if a > 0 and nums[a-1]==nums[a]:
                continue
            b, c = a+1, n-1
            while b < c:
                if nums[a]+nums[b]+nums[c] > 0:
                    c -= 1
                elif nums[a]+nums[b]+nums[c] < 0:
                    b += 1
                else:
                    ans.append([nums[a], nums[b], nums[c]])
                    k, l = b, c
                    while k < c and nums[k] == nums[b]:
                        k += 1
                    print(b, c, k, l ,nums, nums[l], nums[c])
                    while l > b and nums[l] == nums[c]:
                        l -= 1
                    b, c = k, l
        return ans


if __name__ == '__main__':
    print(Solution().threeSum([0,0,0]))
























# @lc code=end

