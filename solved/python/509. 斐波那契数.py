class Solution:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            fi1b = n
        else:
            fi1b = self.fib(n-1)+self.fib(n-2)

        return fi1b

    def fi1b(self):
        print([self.fib(i) for i in range(31)])

if __name__ == '__main__':
    print(Solution().fi1b())