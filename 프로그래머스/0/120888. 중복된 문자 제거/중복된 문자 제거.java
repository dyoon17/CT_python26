import java.util.HashSet;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        HashSet <Character> set = new HashSet<>();
        
        for (int i = 0; i < my_string.length(); i++) {
            if (set.contains(my_string.charAt(i))) {
                continue;
            } else {
                set.add(my_string.charAt(i));
                answer += my_string.charAt(i);
            }
        }
        
        return answer;
    }
}