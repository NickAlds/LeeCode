"""
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明: 
你可以假设 nums 的长度≥ k-1 且k ≥ 1。
"""
class KthLargest:
    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.klist = sorted(nums[:k-1])
        self.k = k
        for i in nums[k-1:]:
            self.add(i)
        
    def add(self, val):
        if len(self.klist)<self.k:
            nkl = [val]+self.klist
        elif val>self.klist[0]:
            self.klist[0] = val
            nkl = self.klist
        else:
            return self.klist[0]
        p = 0
        while 2*p+1<self.k:
            if 2*p+2>=self.k:
                if nkl[p]>nkl[2*p+1]:
                    nkl[p], nkl[2*p+1] = nkl[2*p+1], nkl[p]
                    p = 2*p+1
                else:
                    break
            elif nkl[p]>min(nkl[2*p+1], nkl[2*p+2]):
                if nkl[2*p+1]<=nkl[2*p+2]:
                    nkl[p], nkl[2*p+1] = nkl[2*p+1], nkl[p]
                    p = 2*p+1
                else:
                    nkl[p], nkl[2*p+2] = nkl[2*p+2], nkl[p]
                    p = 2*p+2
            else:
                break
        self.klist = nkl
        return self.klist[0]

import heapq
class KthLargest1:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for i in nums:
            self.add(i)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k :
            heapq.heappush(self.heap,val)
        elif self.heap[0] < val :
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

kl = KthLargest(4, [4,5,8,2])
[2,3,4,5,5,8]
print('rst: ', kl.add(3))
print('rst: ', kl.add(5))
print('rst: ', kl.add(10))
print('rst: ', kl.add(9))
print('rst: ', kl.add(4))
