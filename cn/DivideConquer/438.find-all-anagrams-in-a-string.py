#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (36.75%)
# Total Accepted:    112.9K
# Total Submissions: 307.1K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import Counter
        lp = len(p)
        ls = len(s)
        res = []
        if ls < lp:
            return []
        cp = dict(Counter(p))
        cs = {}
        left = right = 0
        for i, char in enumerate(s):
            if char in cp.keys():
                cs[char] = cs.get(char, 0)+1
                right=i
                #print(left, right, cs)
                #while right-left>lp-1:
                #    if s[left] in cp.keys():
                #        cs[s[left]] -= 1
                #    left += 1
                if right-left == lp-1:
                    if cs == cp:
                        res.append(left)
                    cs[s[left]] -= 1
                    left += 1
            else:
                left = right = i+1
                cs = {}
        return res
print(Solution().findAnagrams("cbaebabacd", "abc"))

