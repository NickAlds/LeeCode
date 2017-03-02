'''
452. Minimum Number of Arrows to Burst Balloons
Description  Submission  Solutions
Total Accepted: 7933
Total Submissions: 18636
Difficulty: Medium
Contributors: abhijeeg
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
Subscribe to see which companies asked this question.
'''
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key = lambda p: p[0])
        temp = [points[0][0], points[-1][-1]]
        cnt = 1
        length = len(points)
        for i, p in enumerate(points):
            maxl = min(p[1], temp[1])
            minl = p[0]
            print minl, maxl
            if maxl < minl:
                temp = p
                cnt += 1
            else:
                temp = [minl, maxl]
        return cnt

print Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])