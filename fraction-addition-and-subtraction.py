#!/usr/bin/env python
#coding: utf-8
"""
592. Fraction Addition and Subtraction Add to List
Description
Hints
Submissions
Solutions
Total Accepted: 1427 Total Submissions: 3065 Difficulty: Medium
Contributors: fallcreek
Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"
Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"
Example 3:
Input:"1/3-1/2"
Output: "-1/6"
Example 4:
Input:"5/3+1/3"
Output: "2/1"
Note:
The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1,10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
Subscribe to see which companies asked this question.
"""
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        expression = expression.replace('-', '+-')
        if expression[0] == '+':
            expression = expression[1:]
        frac_list = expression.split('+')
        frac_sum = (0, 1)
        for frac in frac_list:
            frac = frac.split('/')
            frac = (int(frac[0]), int(frac[1]))
            gcd_m = self.cal_lcm(frac_sum[1], frac[1])
            gcd_s = (frac[0]*gcd_m/frac[1]+frac_sum[0]*gcd_m/frac_sum[1])
            print gcd_m, gcd_s
            if not gcd_s:
                gcd_m = 1
                frac_sum = (0, 1)
            else:
                gcd_sum = self.cal_gcd(gcd_s, gcd_m)
                frac_sum = (gcd_s/gcd_sum, gcd_m/gcd_sum)
            print frac_sum, frac
        return str(frac_sum[0])+'/'+str(frac_sum[1])

    def cal_gcd(self, a, b):
        a, b = abs(a), abs(b)
        if a < b:
            a, b = b, a
        mod = a%b
        while mod:
            a, b = b, mod
            mod = a%b
        return b
    def cal_lcm(self, a, b):
        return a*b/self.cal_gcd(a, b)
s = Solution()
print s.fractionAddition("1/1-7/5-5/2")
