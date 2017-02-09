'''
500. Keyboard Row
Description  Submission  Solutions  Add to List
Total Accepted: 3143
Total Submissions: 5119
Difficulty: Easy
Contributors: Admin
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard
https://leetcode.com/static/images/problemset/keyboard.png

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        newwords = []
        for word in words:
            for row in rows:
                if (set(word.lower())|set(row)) == set(row):
                    newwords.append(word)
                    #print word,row
        return newwords

s1 = Solution()

print s1.findWords(["Hello", "Alaska", "Dad", "Peace"])