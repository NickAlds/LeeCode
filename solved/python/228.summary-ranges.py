#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
from typing import List
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i]-nums[i-1] == 1:
                ans[-1][1] = nums[i]
            else:
                ans.append([nums[i], nums[i]])
        return ["{}->{}".format(a[0], a[1]) if a[0]!=a[1] else str(a[0]) for a in ans]
# @lc code=end
if __name__ == '__main__':
    print(Solution().summaryRanges([0,2,3,4,6,8,9]))
