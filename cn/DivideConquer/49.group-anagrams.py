#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (45.37%)
# Total Accepted:    309.5K
# Total Submissions: 681.4K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#
class Solution:
    def groupAnagrams(self, strs):
        sorted_strs = [''.join(sorted(s)) for s in strs]
        #keys = set(sorted_strs)
        anagrams_dict = {}
        for i, s in enumerate(sorted_strs):
            anagrams_dict[s] = anagrams_dict.get(s, [])+[strs[i]]
        return list(anagrams_dict.values())
