class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        point = 0
        if y > x:
            s = s[::-1]
            x, y = y, x
        stack, t = [], []
        for ch in s:
            if ch == "b" and stack and stack[-1]=="a":
                point += x
                stack.pop(-1)
            else:
                stack.append(ch)
        for ch in stack:
            if ch == "a" and t and t[-1] == "b":
                point += y
                t.pop(-1)
            else:
                t.append(ch)
        return point



if __name__ == '__main__':
    print(Solution().maximumGain("aabbaaxybbaabb", 5, 4))