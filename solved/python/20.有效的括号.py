#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    # 妙解
    def isValid1(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    # 栈
    def isValid(self, s: str) -> bool:
        left = "{[("
        right = "}])"
        lrmap = {right[i]:left[i] for i in range(3)}
        stack = []
        for ch in s:
            if ch in left:
                stack.append(ch)
            elif ch in right and stack and lrmap[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        return True
# @lc code=end
if __name__ == '__main__':
    print(Solution().isValid1("()"))
