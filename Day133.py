#Minimum Platforms

class Solution:    
    def minimumPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        i = 0
        j = 0
        platforms_needed = 0
        max_platforms = 0
        
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1
            else:
                platforms_needed -= 1
                j += 1
            
            max_platforms = max(max_platforms, platforms_needed)
        
        return max_platforms

# Example usage: User input
if __name__ == "__main__":
    n = int(input("Enter the number of trains: "))
    arr = list(map(int, input("Enter the arrival times: ").split()))
    dep = list(map(int, input("Enter the departure times: ").split()))

    sol = Solution()
    result = sol.minimumPlatform(arr, dep)
    print(f"Minimum number of platforms required: {result}")

# Example usage: Inbuilt data
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

sol = Solution()
result = sol.minimumPlatform(arr, dep)
print(f"Minimum number of platforms required (Inbuilt data): {result}")
