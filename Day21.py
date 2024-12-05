#Sort 0s, 1s and 2s


class Solution:
    def sort012(self,arr,n):
    low, mid, high = 0, 0, len(arr) - 1
    
    # Traverse through the array
    while mid <= high:
        if arr[mid] == 0:
            # Swap arr[low] and arr[mid], increment low and mid
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # Just move mid forward
            mid += 1
        else:
            # Swap arr[mid] and arr[high], decrement high
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

# Test cases
print(sortColors([0, 1, 2, 0, 1, 2]))  # Output: [0, 0, 1, 1, 2, 2]
print(sortColors([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))  # Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]




#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends
