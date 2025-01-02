#Subarrays with sum K
class Solution:
    def countSubarrays(self, arr, k):
        count=0
        s=0
        sum_dict={0:1}
        for num in arr:
            s+=num
            if s-k in sum_dict:
                count+=sum_dict[s-k]
            if s in sum_dict:
                sum_dict[s]+=1
            else:
                sum_dict[s]=1
        return count

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
arr = [10, 2, -2, -20, 10]
k = -10
solution = Solution()
print(solution.countSubarrays(arr, k))  # Output: 3
# Example 2
arr = [9, 4, 20, 3, 10, 5]
k = 33
solution = Solution()
print(solution.countSubarrays(arr, k))  # Output: 2
# Example 3
arr = [1, 3, 5]
k = 0
solution = Solution()
print(solution.countSubarrays(arr, k))  # Output: 0

