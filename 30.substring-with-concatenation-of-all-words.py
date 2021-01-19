#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
from lc_types import List
import collections
# @lc code=start
class Solution:
    # 逐个匹配
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n = len(s)
        lenw = len(words)
        step = len(words[0])
        start = 0
        cur_words = [w for w in words]
        while n-start >= lenw*step:
            tmp = start
            while s[tmp:tmp+step] in cur_words:
                cur_words.remove(s[tmp:tmp+step])
                tmp += step
            if not cur_words:
                ans.append(tmp)
                cur_words = [w for w in words]
            elif len(cur_words) < lenw:
                cur_words = [w for w in words]
            start += 1
        return [i-lenw*step for i in ans]

    # 滑动窗口
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        import collections
        a = collections.defaultdict(int)
        maxl = 0
        for r in rectangles:
            cur = min(r)
            a[cur]+=1
            if cur>maxl:
                maxl = cur
        return a[maxl]

    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        a = collections.defaultdict(int)
        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a[nums[i]*nums[j]] += 1
        print(a)
        for v in a.values():
            m = v//2
            if m < 2:
                continue
            ans += m*(m-1)*4
            # print(m, m*(m-1)*4)
        return ans

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxS = 0
        cols = [list(i) for i in zip(*matrix)]
        for col in cols:
            for i in range(m):
                if i >0 and col[i] == 1 and col[i-1] > 0:
                    col[i] = col[i-1]+1
        for i in range(m):
            rv = [col[i] for col in cols]
            rv.sort()
            maxS = max(maxS, max([rv[k]*(n-k) for k in range(n)]))
        return maxS

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(collections) < 3:
            return True
        x1, y1, x2, y2 = coordinates[0], coordinates[1]
        a = (y1-y2)/(x1-x2)
        b = y1-a*x1
        for x, y in coordinates[2:]:
            if y!=a*x+b:
                return False
        return True


# @lc code=end
if __name__ == '__main__':
    print(Solution().largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))
