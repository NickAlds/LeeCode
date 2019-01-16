'''
406. Queue Reconstruction by Height
Description  Submission  Solutions  Add to List
Total Accepted: 16227
Total Submissions: 29734
Difficulty: Medium
Contributors: Admin
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        A = [[i[0],-i[1]] for i in people]
        A.sort()
        B = [i for i in range(len(A))]
        C = [0]*len(A)
        for i in A:
            #print i
            C[B[-i[1]]] = [i[0],-i[1]]
            B.pop(-i[1])
        return C