import functools


class Solution:
    @functools.lru_cache(100)
    def totalMoney(self, n: int) -> int:

        if n == 0:
            return 0
        fn = n%7+n//7 if n%7 else 6+n//7
        # print(n, fn)
        return self.totalMoney(n-1)+fn

if __name__ == '__main__':
    print(Solution().totalMoney(20))

