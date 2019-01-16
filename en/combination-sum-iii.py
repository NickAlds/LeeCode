'''
216. Combination Sum III
Description  Submission  Solutions
Total Accepted: 59102
Total Submissions: 138024
Difficulty: Medium
Contributors: Admin
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if not k:
            return [[]]
        cache = [0]*k
        res = []
        def search(cur, ksum):
            if cur == k:
                if set(cache) not in res:
                    res.append(set(cache))
            else:
                for i in xrange(1, 10):
                    #print cur
                    cache[cur] = i
                    isok = 1
                    if i in cache[:cur] or ksum+i > n or (cur == k-1 and ksum+i != n):
                        isok = 0
                    if isok:
                        #print cache, cur+1
                        search(cur+1, ksum+i)
        if k <= 5:
            search(0, 0)
            return [list(i) for i in res]
        else:
            res = self.combinationSum3(9-k, 45-n)
            return [list(set(range(1, 10))-set(i)) for i in res]

print Solution().combinationSum3(9, 45)
