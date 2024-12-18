# Allocate Minimum Pages
class Solution:
    def findPages(self, arr, k):
        if k > len(arr): 
            return -1
        
        low, high = max(arr), sum(arr)
        
        while low <= high:
            mid = (low + high) // 2
            student_count, current_sum = 1, 0
            
            # Check if it's possible to allocate pages such that no student gets more than 'mid' pages
            for pages in arr:
                current_sum += pages
                if current_sum > mid:
                    student_count += 1
                    current_sum = pages
                    if student_count > k:
                        break
            
            if student_count <= k:
                high = mid - 1
            else:
                low = mid + 1
        
        return low

# Example usage
sol = Solution()
arr = [12, 34, 67, 90]  # Page counts of books
k = 2  # Number of students

result = sol.findPages(arr, k)
print(f"The minimum number of pages the student with the most pages will have: {result}")
