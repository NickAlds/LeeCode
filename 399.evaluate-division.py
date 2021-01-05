#
# @lc app=leetcode id=399                                       lang=python3
#
# [399] Evaluate Division
#
from typing import List
# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        map_a = dict()
        map_b = dict()
        ans = []
        for e in equations:
            map_a[e[0]] = map_a.get(e[0], []).append(tuple(e))
            map_b[e[1]] = map_b.get(e[1], []).append(tuple(e))
        for q in queries:
            if q[1] == q[2]:
                ans.append(1.0)
# @lc code=end

