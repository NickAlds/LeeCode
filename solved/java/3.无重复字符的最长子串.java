class Solution {
    public static int lengthOfLongestSubstring(String s) {
        char[] cc = s.toCharArray();
        List<Character> queue = new ArrayList<Character>();
        int maxl = 0;
        for (char c:cc){
            while (queue.contains(c)){
                queue.remove(0);
            }
            queue.add(c);
            maxl = java.lang.Integer.max(queue.size(), maxl);
        }
        return maxl;
    }
}