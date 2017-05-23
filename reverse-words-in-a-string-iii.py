"""
557. Reverse Words in a String III Add to List
Description
Hints
Submissions
Solutions
Total Accepted: 16705 Total Submissions: 27333 Difficulty: Easy
Contributors: joshpowell
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

Subscribe to see which companies asked this question.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for i, word in enumerate(words):
            r_word = list(word)
            r_word.reverse()
            words[i] = ''.join(r_word)
        return ' '.join(words)
