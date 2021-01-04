class Solution(object):
    def bi_search(self, list, target, left=1):
        start = 0
        end = len(list) - 1
        while end>start:
            mid = (start+end)/2
            if list[mid] < target:
                start = mid+1
            elif target < list[mid]:
                end=mid
            elif left:
                end=mid
            else:
                start=mid+1
        return start

    def waysToSplit1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = []
        cur_sum = 0
        for i in nums:
            sums.append(cur_sum + i)
            cur_sum += i
        len_sum = len(sums)
        total = 0

        for i1, p1 in enumerate(sums):
            if p1 > sums[-1]/3.0 or len_sum-1 - i1 < 2:
                break
            # p2 - p1 >= p1 >>> p2 >= 2p1
            midl = self.bi_search(sums[i1+1:], 2*p1, left=1)+i1+1
            # sunms[-1] - p2 >= p2 - p1 >>> p2 <= (sum[-1]+p1)/2.0
            midr = self.bi_search(sums[i1+1:], (sums[-1]+p1)/2.0, left=0)+i1+1
            print(i1, midl ,midr)
            total += midr - midl
        return total

    # 三指针揭发
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sums = []
        cur_sum = 0
        for i in nums:
            sums.append(cur_sum + i)
            cur_sum += i
        len_sum = len(sums)
        total = 0
        l = r = 0
        for i1, p1 in enumerate(sums):
            if p1 > sums[-1] / 3.0 or len_sum - 1 - i1 < 2:
                break
            l = max(i1 + 1, l)
            r = max(i1 + 1, r)
            while l < len_sum - 1 and sums[l] < 2 * p1:
                l += 1
            while r < len_sum - 1 and 2 * sums[r] <= (sums[-1] + p1):
                r += 1
            if l < r:
                total += r - l
        return total % 1000000007


if __name__ == '__main__':
    print(Solution().waysToSplit([0,0,0,0,0]))
