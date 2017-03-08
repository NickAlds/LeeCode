'''
241. Different Ways to Add Parentheses
Description  Submission  Solutions
Total Accepted: 39228
Total Submissions: 93348
Difficulty: Medium
Contributors: Admin
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''
class Solution(object):
    def diffWaysToCompute(self, input_str):
        """
        :type input: str
        :rtype: List[int]
        """
        if input_str.isdigit():
            return [int(input_str)]
        rstlist = []
        for i, char in enumerate(input_str):
            if char in '*+-':
                pre = self.diffWaysToCompute(input_str[:i])
                suff = self.diffWaysToCompute(input_str[i+1:])
                for j in pre:
                    for k in suff:
                        if char == '+':
                            rstlist.append(j+k)
                        if char == '*':
                            rstlist.append(j*k)
                        if char == '-':
                            rstlist.append(j-k)
        return rstlist
