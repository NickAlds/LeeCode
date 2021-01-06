#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        
        cur = " "
        ans = 0
        flag = 1
        for char in s:
            # print(cur+char+"1")
            if char==" " and cur == " ":
                continue
            if char and char in "+-" and cur == " ":
                flag = 1 if char == "+" else -1
                cur = char
            elif char and char in "1234567890" and cur in "1234567890+- ":
                ans = ans*10 + int(char)
                cur = char
            else:
                break
        MAX = 2**31-1
        MIN = -1*MAX-1
        if MIN <= ans*flag <= MAX:
            return ans*flag
        elif ans*flag < MIN:
            return MIN
        else:
            return MAX
            
# @lc code=end
print(Solution().myAtoi("42"))

