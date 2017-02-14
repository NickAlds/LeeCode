'''
451. Sort Characters By Frequency
Description  Submission  Solutions  Add to List
Total Accepted: 17699
Total Submissions: 35385
Difficulty: Medium
Contributors: stickypens
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqdict = {}
        for i in s:
            if i in freqdict.keys():
                freqdict[i] += 1
            else:
                freqdict[i] = 1
        sortdict = {}
        for i in freqdict:
            if freqdict[i] in sortdict.keys():
                sortdict[freqdict[i]] += i*freqdict[i]
            else:
                sortdict[freqdict[i]] = i*freqdict[i]
        length = len(s)
        res = ''
        #print freqdict
        freq = sortdict.keys()
        freq.sort()
        for i in freq:
            #print i
            res = sortdict[i] + res
        return res

s1 = Solution()

s ="tree"

print s1.frequencySort(s)