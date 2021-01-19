#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import List


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int], target, start) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        if sum(nums[:3])>target or sum(nums[-3:])<target:
            return []
        ans = []
        for a in range(n):
            if a > 0 and nums[a-1]==nums[a]:
                continue
            b, c = a+1, n-1
            while b < c:
                if nums[a]+nums[b]+nums[c] > target:
                    c -= 1
                elif nums[a]+nums[b]+nums[c] < target:
                    b += 1
                else:
                    ans.append([start, nums[a], nums[b], nums[c]])
                    k, l = b, c
                    while k < c and nums[k] == nums[b]:
                        k += 1
                    # print(b, c, k, l ,nums, nums[l], nums[c])
                    while l > b and nums[l] == nums[c]:
                        l -= 1
                    b, c = k, l
        return ans

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 4:
            return []
        ans = []
        for a in range(n):
            if a > 0 and nums[a-1]==nums[a]:
                continue
            ans += self.threeSum(nums[a+1:], target-nums[a], nums[a])
        return ans

    # O(n^2)
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        d={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                d.setdefault(nums[i]+nums[j],[]).append((i,j))
        result=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for a,b in d.get(target-nums[i]-nums[j],[]):
                    temp={i,j,a,b}
                    if len(temp)==4:
                        result.add(tuple(sorted(nums[t] for t in temp)))
        return [list(i) for i in result]
# @lc code=end

