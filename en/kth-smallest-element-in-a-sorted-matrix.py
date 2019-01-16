'''
378. Kth Smallest Element in a Sorted Matrix
Description  Submission  Solutions
Total Accepted: 28649
Total Submissions: 65794
Difficulty: Medium
Contributors: Admin
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
'''
#what solves this problem may be called "the Matrix Binary Search"
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid, cnt, j = (low+high)//2, 0, len(matrix)
            for row in matrix:
                while j > 0 and row[j-1] > mid:
                    j -= 1
                cnt += j
            if cnt >= k:
                high = mid
            else:
                low = mid+1
        return low
        