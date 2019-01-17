"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = '([{'
        right = ')]}'
        lrmap = {right[i]:left[i] for i in range(3)}
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if not len(stack) or stack.pop() != lrmap[i]:
                    return False
        return not stack
