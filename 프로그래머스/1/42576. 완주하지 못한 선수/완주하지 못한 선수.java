import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> list = new HashMap<>();
        
        for (int i = 0; i < participant.length; i++) {
            String name = participant[i];
            int count = list.getOrDefault(name, 0);
            list.put(name, count + 1);
        }
        
        for (int i = 0; i < completion.length; i++) {
            String name = completion[i];
            int count = list.getOrDefault(name, 0);
            if (list.containsKey(name)) {
                list.put(name, count - 1);
            }
        }
        
        for (String name : list.keySet()) {
                if (list.get(name) != 0) {
                    answer = name;
                }
            }
            
        return answer;
    }
}