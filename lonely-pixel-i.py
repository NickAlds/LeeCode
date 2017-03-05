'''
531. Lonely Pixel I
Description  Submission  Solutions
Total Accepted: 1408
Total Submissions: 3135
Difficulty: Medium
Contributors: fallcreek
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].
Subscribe to see which companies asked this question.
'''
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        leni = len(picture)
        lenj = len(picture[0])
        sumi = [sum([picture[i][j] == 'B' for i in xrange(leni)]) for j in xrange(lenj)]
        sumj = [sum([picture[i][j] == 'B' for j in xrange(lenj)]) for i in xrange(leni)]
        #print sumi, sumj,leni,lenj
        return sum([picture[i][j] == 'B' and sumi[j] == 1 and sumj[i] == 1 for j in xrange(lenj) for i in xrange(leni)])
    def findLonelyPixel1(self, picture):
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') for col in zip(*picture))
print Solution().findLonelyPixel(["BBB"])