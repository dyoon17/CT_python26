import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        HashSet<Integer> set = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i])) {
                continue;
            } else {
                set.add(nums[i]);
            }
        }
        
        if (set.size() < (nums.length / 2)) {
            answer = set.size();
        } else {
            answer = nums.length / 2;
        }
            
        return answer;
    }
}