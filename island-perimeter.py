"""
463. Island Perimeter
Description  
Submission  
Discussion  
Add to List
Total Accepted: 22464 Total Submissions: 40304 Difficulty: Easy Contributors: amankaraj
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
https://leetcode.com/static/images/problemset/island.png
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lengthi = len(grid)
        lengthj = len(grid[0])
        cnt = 0
        for i in range(lengthi):
            for j in range(lengthj):
                if grid[i][j] and not i:
                    cnt+=1
                if grid[i][j] and not j:
                    cnt+=1
                if i<lengthi-1 and grid[i][j]^grid[i+1][j]:
                    cnt+=1
                if j<lengthj-1 and grid[i][j]^grid[i][j+1]:
                    cnt+=1
                if (grid[i][j] and i == lengthi-1):
                    cnt+=1
                if grid[i][j] and j == lengthj-1:
                    cnt+=1
        return cnt

s = Solution()
test = [[1],[0]]
print s.islandPerimeter(test)