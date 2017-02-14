'''
481. Magical String
Description  Submission  Solutions  Add to List
Total Accepted: 4250
Total Submissions: 9146
Difficulty: Medium
Contributors: DonaldTrump
A magical string S consists of only '1' and '2' and obeys the following rules:

The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.

The first few elements of string S is the following: S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2	2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the S itself.

Given an integer N as input, return the number of '1's in the first N number in the magical string S.

Note: N will not exceed 100,000.

Example 1:
Input: 6
Output: 3
Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
'''
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        cntstr = [1, 2]+[0]*(n-2)
        cnt, i, onecnt = 1, 1, 1
        while cnt < n:
            if i%2 == 1:
                if cntstr[i] == 2 and cnt < n-1 :
                    cntstr[cnt], cntstr[cnt+1] = 2, 2
                else:
                    cntstr[cnt] = 2
            else:
                if cntstr[i] == 2 and cnt < n-1:
                    cntstr[cnt], cntstr[cnt+1] = 1, 1
                    onecnt += 2
                else:
                    cntstr[cnt] = 1
                    onecnt += 1
            cnt += cntstr[i]
            i += 1
        return onecnt