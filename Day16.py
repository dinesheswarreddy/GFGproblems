#Anagram

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        if(sorted(s1)==sorted(s2)):
            return True
        else:
            return False

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")
