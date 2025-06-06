//Search Pattern (Rabin-Karp Algorithm)

import java.util.*;

class Solution {
    static final int d = 256;
    static final int q = 101;

    ArrayList<Integer> search(String pat, String txt) {
        ArrayList<Integer> result = new ArrayList<>();

        int M = pat.length();
        int N = txt.length();
        int i, j;
        int p = 0; // hash for pattern
        int t = 0; // hash for text
        int h = 1;

        for (i = 0; i < M - 1; i++)
            h = (h * d) % q;

        for (i = 0; i < M; i++) {
            p = (d * p + pat.charAt(i)) % q;
            t = (d * t + txt.charAt(i)) % q;
        }

        for (i = 0; i <= N - M; i++) {
            if (p == t) {
                for (j = 0; j < M; j++) {
                    if (txt.charAt(i + j) != pat.charAt(j))
                        break;
                }

                if (j == M)
                    result.add(i + 1); // 1-based indexing
            }

            if (i < N - M) {
                t = (d * (t - txt.charAt(i) * h) + txt.charAt(i + M)) % q;
                if (t < 0)
                    t = (t + q);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Enter the text string:");
        String text = sc.nextLine();

        System.out.println("Enter the pattern to search:");
        String pattern = sc.nextLine();

        ArrayList<Integer> positions = sol.search(pattern, text);
        System.out.println("Pattern found at positions (user input): " + positions);

        // ---- Inbuilt Example ----
        String builtInText = "geeksforgeeks";
        String builtInPattern = "geek";
        ArrayList<Integer> builtInPositions = sol.search(builtInPattern, builtInText);
        System.out.println("Pattern found at positions (inbuilt test): " + builtInPositions);
    }
}
