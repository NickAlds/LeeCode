'''
401. Binary Watch Add to List
Description  Submission  Solutions
Total Accepted: 21837
Total Submissions: 49394
Difficulty: Easy
Contributors: Admin
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        rlist = []
        i = 0
        listh, lism = self.translist()
        while i <= num and i < 4:
             j = num - i
             if j > 5:
                 continue
             rlist += self.reslist(listh[i], lism[j])
             i += 1
        return rlist
    def translist(self):
        listh = [[0], [1,2,4,8], [3,5,9,6,10], [11,7]]
        listm = [[] for i in xrange(6)]
        rlist = []
        listm[0] = [0]
        listm[1] = [1,2,4,8,16,32]
        listm[5] = [59,55,47,31]
        for i in xrange(5):
            for j in xrange(i+1,6):
                listm[2].append(listm[1][i]+listm[1][j])
        listm[4] = [63 - i for i in listm[2] if i > 3 ]
        for i in xrange(4):
            for j in xrange(i+1, 5):
                for k in xrange(j+1,6):
                    listm[3].append(listm[1][i]+listm[1][j]+listm[1][k])
        return listh, listm
    def reslist(self, list1, list2):
        rlist = []
        for i in list1:
            for j in list2:
                rlist.append(str(i)+':'+format(j, '02d'))
        return rlist

print Solution().readBinaryWatch(1)
