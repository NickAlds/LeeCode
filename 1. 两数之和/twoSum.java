import java.util.HashMap;

class Solution{
    public static int[] twoSum(int[] nums, int target) {
        int[] ret = {};
        HashMap<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
        int index=0;
        for (int num:nums){
            if(hashmap.containsKey(target-num)){
                int diff_index = hashmap.get(target-num);
                return new int[] {diff_index, index};
            }
            else{
                hashmap.put(num, index);
            }
            index++;
        }
        return ret;
    }
}