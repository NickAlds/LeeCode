class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        if str(s) == str(t):
            return True
        else:
            return False

solution = Solution()
print solution.isAnagram("cat","tac")
