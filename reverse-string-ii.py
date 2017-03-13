'''
541. Reverse String II
DescriptionSubmissionsSolutions
Total Accepted: 2299
Total Submissions: 5026
Difficulty: Easy
Contributors: Stomach_ache
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

'''
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        s = '0'+s
        while len(s) > 2*k+1:
            res += s[k:0:-1]+s[k+1:2*k+1]
            print res
            s = '0'+s[2*k+1:]
        if len(s) > k:
            res += s[k:0:-1]+s[k+1:]
        else:
            res += s[::-1][:-1]
        return res
print Solution().reverseStr('abcdefghm', 2)
