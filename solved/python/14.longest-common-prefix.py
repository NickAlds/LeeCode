#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = strs[0]
        for s in strs:
            while not s.startswith(cur):
                cur = cur[:-1]
                if not cur:
                    return ""
        return cur
# @lc code=end

