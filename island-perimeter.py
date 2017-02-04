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