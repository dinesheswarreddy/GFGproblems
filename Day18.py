#Search Pattern (KMP-Algorithm)
def find_occurrences(t, p):
    indices = []
    for i in range(len(t) - len(p) + 1):
        if t[i:i + len(p)] == p:
            indices.append(i)
    return indices

# Example usage:
txt1 = "abcab"
pat1 = "ab"
print(find_occurrences(txt1, pat1))  # Output: [0, 3]

txt2 = "abesdu"
pat2 = "edu"
print(find_occurrences(txt2, pat2))  # Output: []

txt3 = "aabaacaadaabaaba"
pat3 = "aaba"
print(find_occurrences(txt3, pat3))  # Output: [0, 9, 12]
