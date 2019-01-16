'''
447. Number of Boomerangs
Description  Submission  Solutions
Total Accepted: 14369
Total Submissions: 33160
Difficulty: Easy
Contributors: alexander54
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cache = {}
        length = len(points)
        if length < 3:
            return 0
        distances = [{} for i in xrange(length)]
        cnt = 0
        for i in xrange(length-1):
            for j in xrange(i+1, length):
                distance = (points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                if distances[i].has_key(distance):
                    distances[i][distance] += 1
                else:
                    distances[i][distance] = 1
                if distances[j].has_key(distance):
                    distances[j][distance] += 1
                else:
                    distances[j][distance] = 1
            for dist in distances[i]:
                n = distances[i][dist]
                cnt += n*(n-1)
            #print distances[i], cnt
        for dist in distances[i+1]:
            n = distances[i+1][dist]
            cnt += n*(n-1)
        #print distances[i], cnt
        return cnt
print Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]])