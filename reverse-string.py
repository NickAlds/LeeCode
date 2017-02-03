"""
344. Reverse String   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 127538
Total Submissions: 220938
Difficulty: Easy
Contributors: Admin
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""
import time
class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])


class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]
teststr = "qqwe"
s = Solution()
s1 = SolutionClassic()
s2 = SolutionPythonic()

t1 = int(time.time()*10000000)
s.reverseString(teststr)
t2 = int(time.time()*10000000)
s1.reverseString(teststr)
t3 = int(time.time()*10000000)
s2.reverseString(teststr)
t4 = int(time.time()*10000000)

print t2-t1, t3-t2, t4-t3