#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
from lc_types import List
import collections
# @lc code=start
class Solution:
    # 逐个匹配
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n = len(s)
        lenw = len(words)
        step = len(words[0])
        start = 0
        cur_words = [w for w in words]
        while n-start >= lenw*step:
            tmp = start
            while s[tmp:tmp+step] in cur_words:
                cur_words.remove(s[tmp:tmp+step])
                tmp += step
            if not cur_words:
                ans.append(tmp)
                cur_words = [w for w in words]
            elif len(cur_words) < lenw:
                cur_words = [w for w in words]
            start += 1
        return [i-lenw*step for i in ans]

    # 滑动窗口






# @lc code=end
if __name__ == '__main__':
    print(Solution().largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))
