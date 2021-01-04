#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x >= 0 else -1
        x *= flag
        list = []
        while x:
            # print(x)
            list.append(x % 10)
            x //= 10
        ans = 0
        # print(list)
        for i in list:
            ans += i
            ans *= 10
        if -1*pow(2, 31) <= ans//10*flag <= pow(2, 31):
            return ans//10*flag
        else:
            return 0
        
# @lc code=end
if __name__ == '__main__':
    print(Solution().reverse(-1240))

