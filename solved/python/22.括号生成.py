#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def back(path, l, r):
            if len(path) == 2*n:
                ans.append(path)
                return
            if l < n:
                back(path+"(", l+1, r)
            if l > r:
                back(path+")", l, r+1)
        back("", 0, 0)
        return ans
# @lc code=end
if __name__ == '__main__':
    print(Solution().generateParenthesis(3))

