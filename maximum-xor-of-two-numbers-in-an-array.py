'''
421. Maximum XOR of Two Numbers in an Array
Description  Submission  Solutions
Total Accepted: 8875
Total Submissions: 20247
Difficulty: Medium
Contributors: shen5630
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''
class Solution(object):
    def findMaximumXOR(self, nums):
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
            #print bin(answer)[2:]
        return answer

print Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
