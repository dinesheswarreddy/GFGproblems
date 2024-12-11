#Merge Without Extra Space
class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        merged = []
        i, j = 0, 0
        
        while i < n and j < m:
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1

        while i < n:
            merged.append(a[i])
            i += 1
        while j < m:
            merged.append(b[j])
            j += 1

        a[:n] = merged[:n]
        b[:m] = merged[n:]


if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))
