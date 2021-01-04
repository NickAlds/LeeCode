#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#

# @lc code=start
from typing import List


class Solution:

    def largeGroupPositions(self, s: str) -> List[List[int]]:
        cur = ''
        cur_len = 0
        ans = []
        # 哨兵
        s += "@"
        for i in range(len(s)):
            if s[i] != cur:
                if cur_len >= 3:
                    ans.append([i-cur_len, i-1])
                cur = s[i]
                cur_len = 1
            else:
                cur_len += 1
        return ans
# @lc code=end
if __name__ == '__main__':
    print(Solution().largeGroupPositions("aaa"))
