'''
347. Top K Frequent Elements
Description  Submission  Solutions  Add to List
Total Accepted: 49861
Total Submissions: 107381
Difficulty: Medium
Contributors: Admin
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
class SolutionMine(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqdict = {}
        for i in nums:
            if i in freqdict.keys():
                freqdict[i] += 1
            else:
                freqdict[i] = 1
        freqindex = {}
        for i in freqdict:
            if freqindex.has_key(freqdict[i]):
                freqindex[freqdict[i]] += [i]
            else:
                freqindex[freqdict[i]] = [i]
        index = freqindex.keys()
        index.sort()
        i, cnt = 0, 0
        res = []
        length = len(index)
        while cnt < k:
            res += freqindex[index[length-1-i]]
            cnt += len(freqindex[index[length-1-i]])
            i += 1
        return res
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        y = sorted(c.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in y[:k]]

s1 = Solution()

print s1.topKFrequent([5,2,5,3,5,3,1,1,3], 2) 