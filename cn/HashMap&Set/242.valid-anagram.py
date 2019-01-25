#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms  
# Easy (50.40%)
# Total Accepted:    287.6K
# Total Submissions: 570.6K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#
class Solution1:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in count_s:
                count_s[i] = 1
            else:
                count_s[i] += 1
        for i in t:
            if i not in count_s:
                return False
            else:
                count_s[i] -= 1
        return not any(count_s.values())

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

#s = Solution()
#s.isAnagram("anagram","nagaram")



