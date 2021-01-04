class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        countmap = dict()
        powers2 = [pow(2, i) for i in range(22)]
        for i in deliciousness:
            countmap[i] = countmap.get(i, 0) + 1
        total = 0
        for key in countmap:
            for p2 in powers2:
                if p2-key in countmap:
                    if p2 - key == key:
                        total += countmap[key]*(countmap[key]-1)/2
                    else:
                        total += countmap[key]*countmap[p2-key]
            countmap[key] = 0
        return total%(pow(10, 9)+7)


if __name__ == '__main__':
    print Solution().countPairs([1,3,5,7,9])
