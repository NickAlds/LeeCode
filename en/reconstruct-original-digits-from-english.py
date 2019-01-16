'''
423. Reconstruct Original Digits from English
Description  Submission  Solutions
Total Accepted: 7543
Total Submissions: 17546
Difficulty: Medium
Contributors: Admin
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
'''
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cache = {}
        cnt = [0]*10
        res = ''
        charpool = 'egfihonsrutwvxz'
        for i in charpool:
            cache[i] = 0
        for i in s:
            cache[i] += 1
        cnt[0] = cache['z']
        cnt[2] = cache['w']
        cnt[4] = cache['u']
        cnt[6] = cache['x']
        cnt[8] = cache['g']
        cnt[3] = cache['h'] - cache['g']
        cnt[5] = cache['f'] - cache['u']
        cnt[7] = cache['s'] - cache['x']
        cnt[1] = cache['o'] - cnt[0] - cnt[2] - cnt[4]
        cnt[9] = cache['n'] - cnt[1] - cnt[7]
        for i in xrange(10):
            res += str(i)*cnt[i]
        return res

print Solution().originalDigits("fviefuro")
