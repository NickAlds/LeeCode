#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        midl =  midr = (l1+l2)//2
        if not (l1+l2)%2:
            midl = midr - 1
        cur = 0.0
        p1 = p2 = l3 = 0
        nums3 = []
        while p1 < l1 and p2 < l2:
            if nums1[p1]<nums2[p2]:
                nums3.append(nums1[p1])
                p1 += 1
            else:
                nums3.append(nums2[p2])
                p2 += 1
        nums3 += nums1[p1:] if p1 < l1 else nums2[p2:]
        return (nums3[midl]+nums3[midr])/2


# print(Solution().findMedianSortedArrays([1,3], [2]))

# @lc code=end

