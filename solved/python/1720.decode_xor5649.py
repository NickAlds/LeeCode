from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in encoded:
            ans.append(ans[-1]^i)
        return ans

if __name__ == '__main__':
    print(Solution().decode([6,2,7,3], 4))