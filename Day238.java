//Find the longest string
import java.util.*;

public class Main {

    // Optimized function to find the longest valid string
    public static String longestString(String[] words) {
        Set<String> validWords = new HashSet<>();
        Arrays.sort(words); // Sort lexicographically
        String longest = "";
        validWords.add(""); // Empty string acts as a base case

        for (String word : words) {
            String prefix = word.substring(0, word.length() - 1);
            if (validWords.contains(prefix)) {
                validWords.add(word);
                if (word.length() > longest.length() || 
                    (word.length() == longest.length() && word.compareTo(longest) < 0)) {
                    longest = word;
                }
            }
        }

        return longest;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // ---- User Input Example ----
        System.out.println("Enter number of words:");
        int n = sc.nextInt();
        sc.nextLine(); // Consume newline

        String[] userWords = new String[n];
        System.out.println("Enter the words:");
        for (int i = 0; i < n; i++) {
            userWords[i] = sc.nextLine();
        }

        String resultUserInput = longestString(userWords);
        System.out.println("Longest valid string (user input): " + resultUserInput);

        // ---- Inbuilt Example ----
        String[] inbuiltWords = {"p", "pr", "pro", "probl", "problem", "pros", "process", "processor"};
        String resultInbuilt = longestString(inbuiltWords);
        System.out.println("Longest valid string (inbuilt example): " + resultInbuilt);
    }
}
