'''
383. Ransom Note
Description  Submission  Solutions  Add to List
Total Accepted: 41449
Total Submissions: 89634
Difficulty: Easy
Contributors: Admin
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictm ,dictr = {}, {}
        for i in magazine:
            if dictm.has_key(i):
                dictm[i] += 1
            else:
                dictm[i] = 1
        for i in ransomNote:
            if dictr.has_key(i):
                dictr[i] += 1
            else:
                dictr[i] = 1
            if not dictm.has_key(i) or dictr[i] > dictm[i]:
                return False
        return True
