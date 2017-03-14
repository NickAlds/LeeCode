'''
539. Minimum Time Difference
DescriptionSubmissionsSolutions
Total Accepted: 2042
Total Submissions: 4673
Difficulty: Medium
Contributors: fallcreek
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.

'''
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        plist = []
        for i in timePoints:
            point = int(i[:2])*60+int(i[3:5])
            if point not in plist:
                plist.append(point)
            else:
                return 0
        plist.sort()
        last = plist[-1]-24*60
        mini = 1500
        for i in plist:
            cur = i - last
            if cur == 1:
                return 1
            last = i
            if cur < mini:
                mini = cur
        return mini
