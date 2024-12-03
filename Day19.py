#Min Chars to Add for Palindrome
class Solution:
    def minChar(self, s):
        #Write your code here
        r = s[::-1]
        c = s + "#" + r
        n = len(c)
        lps = [0] * n
        j = 0
    
        for i in range(1, n):
            while j > 0 and c[i] != c[j]:
                j = lps[j - 1]
        
            if c[i] == c[j]:
                j += 1
        
            lps[i] = j
    
        return len(s) - lps[-1]
