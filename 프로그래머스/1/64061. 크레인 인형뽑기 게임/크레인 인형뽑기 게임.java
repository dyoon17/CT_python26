import java.util.ArrayDeque;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        
        for (int i = 0; i < moves.length; i++) {
            int col = moves[i] - 1;
            
            for (int j = 0; j < board.length; j++) {
                int doll = board[j][col];
                
                if (doll == 0) {
                    continue;
                } 
                
                if (stack.isEmpty()) {
                   stack.push(doll); 
                } else {
                    if (stack.peek() == doll) {
                        stack.pop();
                        answer += 2;
                    } else {
                        stack.push(doll);
                    }
                }
                
                board[j][col] = 0;
                break;
            }
        }

        return answer;
    }
}