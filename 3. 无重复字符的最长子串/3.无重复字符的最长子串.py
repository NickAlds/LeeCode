#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    # 我的滑动窗口 168 ms 15 MB
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = end = 0
        while end < len(s) - 1:
            char_set = set(s[start: end+1])
            if len(char_set) == end-start+1 and s[end+1] not in char_set:
                end += 1
            else:
                start += 1
                end += 1
        return end - start + 1
    # 别人的滑动窗口 96 ms 14.7 MB
    def lengthOfLongestSubstring1(self, s: str) -> int:
        queue = list()
        maxl = 0
        for char in s:
            while char in queue:
                queue.pop(0)
            queue.append(char)
            maxl = max(len(queue), maxl)
            # print(queue)
        return maxl
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("aasdafsafsaasdgsadsajk"))
# @lc code=end

