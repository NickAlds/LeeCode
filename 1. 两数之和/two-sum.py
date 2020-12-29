class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = dict()
        for i, num in enumerate(nums):
            index_map[num] = index_map.get(num, [])+[i]

        for num in index_map:
            if target==2*num:
                if len(index_map[num])>1:
                    return index_map[num]
            elif target-num in index_map:
                return index_map[num]+index_map[target-num]
        return []