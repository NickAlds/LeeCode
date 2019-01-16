'''
387. First Unique Character in a String
Description  Submission  Solutions
Total Accepted: 44550
Total Submissions: 97502
Difficulty: Easy
Contributors: Admin
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for index, string in enumerate(s):
            if d.has_key(string):
                d[string] = -1
            else:
                d[string] = index
        for i in s:
            if d[i] > -1:
                return d[i]
        return -1

print Solution().firstUniqChar("leetcode")