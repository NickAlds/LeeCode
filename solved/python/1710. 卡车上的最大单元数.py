class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        unitmap = dict()
        for bt in boxTypes:
            unitmap[bt[1]] = bt[0]+unitmap.get(bt[1], 0)
        sizes = unitmap.keys()
        sizes.sort()
        # print sizes
        total_units = 0
        while truckSize > 0 and sizes:
            # print sizes[-1], sizes, truckSize, unitmap[sizes[-1]]
            if unitmap[sizes[-1]] > truckSize:
                total_units += truckSize*sizes[-1]
                truckSize = 0
            else:
                total_units += sizes[-1]*unitmap[sizes[-1]]
                truckSize -= unitmap[sizes[-1]]
                sizes.pop()
        return total_units


if __name__ == '__main__':

    print Solution().maximumUnits([[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]], 13)


