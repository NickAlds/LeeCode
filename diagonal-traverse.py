'''
498. Diagonal Traverse
Description  Submission  Solutions
Total Accepted: 2654
Total Submissions: 5786
Difficulty: Medium
Contributors: nberserk
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:
https://leetcode.com/static/images/problemset/diagonal_traverse.png
Note:
The total number of elements of the given matrix will not exceed 10,000.
'''
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        i, j = 0, 0
        lengthi = len(matrix)
        if lengthi == 0:
            return []
        lengthj = len(matrix[0])
        rlist = []
        while i < lengthi and j < lengthj:
            rlist.append(matrix[i][j])
            place = i+j
            if place%2 == 0:
                if i == 0 and j < lengthj - 1:
                    j += 1
                elif j == lengthj - 1 and i < lengthi - 1:
                    i += 1
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 and i < lengthi - 1:
                    i += 1
                elif i == lengthi - 1 and j < lengthj - 1:
                    j += 1
                else:
                    j -= 1
                    i += 1
        return rlist
