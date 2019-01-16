'''
516. Longest Palindromic Subsequence
Description  Submission  Solutions
Total Accepted: 4178
Total Submissions: 9974
Difficulty: Medium
Contributors: Stomach_ache
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
Subscribe to see which companies asked this question.
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]*n for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(n-i):
                if j == j+i:
                    dp[j][j+i] = 0
                elif s[j] == s[i+j]:
                    dp[j][j+i] = 2+dp[j+1][j+i-1]
                else:
                    dp[j][j+i] = max(dp[j+1][j+i], dp[j][j+i-1])
        return dp[0][n-1]
print Solution().longestPalindromeSubseq("bbbab")

