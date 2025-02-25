import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();

        int[] days = new int[progresses.length];
        for (int i = 0; i < progresses.length; i++) {
            int remainingProgress = 100 - progresses[i];
            double numberOfDaysRequired = (double) remainingProgress / speeds[i];
            days[i] = (int) Math.ceil(numberOfDaysRequired);
        }
        int maxDay = days[0];
        int functionCount = 1;;
        for (int i = 1; i < days.length; i++) {
            if (days[i] <= maxDay) {
                functionCount++;
                continue;
            }
            maxDay = days[i];
            answer.add(functionCount);
            functionCount = 1;
        }
        answer.add(functionCount);
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}