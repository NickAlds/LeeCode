'''
477. Total Hamming Distance
Description  Submission  Solutions
Total Accepted: 8753
Total Submissions: 19130
Difficulty: Medium
Contributors: kevin.xinzhao@gmail.com
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
'''
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, i, j = 0, 0, 0
        #print format(6, '032b')
        cntlist = [[0, 0] for i in xrange(32)]
        for i in nums:
            for j in xrange(32):
                cntlist[j][i%2] += 1
                i /= 2
        return sum(x*y for (x, y) in cntlist)

s1 = Solution()
test = [4,14,4,14]
print s1.totalHammingDistance(test)