'''
22. Generate Parentheses
Description  Submission  Solutions
Total Accepted: 131092
Total Submissions: 307772
Difficulty: Medium
Contributors: Admin
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''
class Solution(object):
    cache = {1:['()'],2:['(())', '()()']}
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n+1)]
        dp[0].append('')
        for i in range(n+1):
            for j in range(i):
                dp[i] += ['('+ x +')'+ y for x in dp[j] for y in dp[i-1-j] ]
        return dp[n]
print Solution().generateParenthesis(2)