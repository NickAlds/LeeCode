'''
409. Longest Palindrome
Description  Submission  Solutions
Total Accepted: 28607
Total Submissions: 64173
Difficulty: Easy
Contributors: Admin
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dict_s = {}
        j, cnt = 0, 0
        while  j < length:
            if dict_s.has_key(s[j]):
                dict_s[s[j]] += 1
            else:
                dict_s[s[j]] = 1
            j += 1
        for i in dict_s:
            if dict_s[i]%2:
                cnt += 1
        return length - cnt + bool(cnt)
print Solution().longestPalindrome('abccccdd')
