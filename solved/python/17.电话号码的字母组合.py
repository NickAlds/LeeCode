#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import List
import functools
# @lc code=start
class Solution:
    @functools.lru_cache(100)
    def letterCombinations(self, digits: str) -> List[str]:
        dmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        if digits in dmap.keys():
            return dmap[digits]
        n = len(digits)
        l = self.letterCombinations(digits[:n//2])
        r = self.letterCombinations(digits[n//2:])
        return [i+j for i in l for j in r]
# @lc code=end
if __name__ == '__main__':
    print(len(Solution().letterCombinations("23456")))
