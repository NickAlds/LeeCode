#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List
# @lc code=start


class Solution:
    # 暴力 超时
    def maxArea1(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for i in range(n-1):
            for j in range(i+1, n):
                max_area = max(max_area, (j-i)*min(height[i], height[j]))
        return max_area

    # 双指针
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        i = 0
        j = n - 1
        while i < j:
            area = min(height[i], height[j])*(j-i)
            max_area = max(max_area, area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area

# @lc code=end
if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
