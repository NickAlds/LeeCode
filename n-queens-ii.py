class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.tot = 0
        pos = [-1]*n
        def search(cur):
            if cur == n:
                self.tot += 1
            else:
                for i in xrange(n):
                    isok = 1
                    pos[cur] = i
                    for j in xrange(cur):
                        if i == pos[j] or i+cur == pos[j]+j or i-cur == pos[j]-j:
                            isok = 0
                            break
                    if isok:
                        search(cur+1)
        search(0)
        return self.tot
class Solutionq(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.tot = 0
        vis = [[0]*n*2 for i in xrange(3)]
        def search(cur):
            if cur == n:
                self.tot += 1
            else:
                for i in xrange(n):
                    if not vis[0][i] and not vis[1][i+cur] and not vis[2][cur-i+n]:
                        vis[0][i], vis[1][i+cur], vis[2][cur-i+n] = 1, 1, 1
                        search(cur+1)
                        vis[0][i], vis[1][i+cur], vis[2][cur-i+n] = 0, 0, 0
        search(0)
        return self.tot
print Solutionq().totalNQueens(8)

