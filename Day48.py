#Print Anagrams Together
class Solution:
    def anagrams(self, arr):
        groups={}
        for word in arr:
            key=''.join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key]=[word]
        return list(groups.values())

t = int(input())
for tcs in range(t):
    words = input().split()
    ob = Solution()
    ans = ob.anagrams(words)
    for grp in sorted(ans):
        for word in grp:
            print(word, end=' ')
        print()
# Example 1
arr1 = ["act", "god", "cat", "dog", "tac"]
output = groupAnagrams(arr1)
for group in output:
    print(" ".join(group))

# Example 2
arr2 = ["no", "on", "is"]
output = groupAnagrams(arr2)
for group in output:
    print(" ".join(group))

# Example 3
arr3 = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
output = groupAnagrams(arr3)
for group in output:
    print(" ".join(group))
