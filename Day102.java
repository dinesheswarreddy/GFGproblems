//Stock span problem
import java.util.*;

class Solution {
    public ArrayList<Integer> calculateSpan(int[] prices) {
        Stack<Integer> indices = new Stack<>();
        ArrayList<Integer> spans = new ArrayList<>();
        
        for (int i = 0; i < prices.length; i++) {
            while (!indices.isEmpty() && prices[indices.peek()] <= prices[i]) {
                indices.pop();
            }
            
            int span = (indices.isEmpty()) ? i + 1 : i - indices.peek();
            spans.add(span);
            
            indices.push(i);
        }
        
        return spans;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Inbuilt example
        int[] inbuiltPrices = {100, 80, 60, 70, 60, 75, 85};
        ArrayList<Integer> inbuiltSpan = solution.calculateSpan(inbuiltPrices);
        System.out.println("Inbuilt Example Span: " + inbuiltSpan);
        
        // User input example
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of days: ");
        int n = scanner.nextInt();
        
        int[] userPrices = new int[n];
        System.out.println("Enter the prices for each day: ");
        for (int i = 0; i < n; i++) {
            userPrices[i] = scanner.nextInt();
        }
        
        ArrayList<Integer> userSpan = solution.calculateSpan(userPrices);
        System.out.println("User Input Span: " + userSpan);
    }
}
