#Max Circular Subarray Sum
#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    def kadane(arr):
        max_sum = current_sum = arr[0]
        for num in arr[1:]:
            max_sum = max(num, max_sum + num)
            current_sum = max(current_sum,max_sum)
        return current_sum
    
    max_kadane=kadane(arr)
    total_sum=sum(arr)
    min_normal = [-x for x in arr]
    max_circular=total_sum+kadane(min_normal)
    if max_circular == 0:
        return max_kadane
    return max(max_kadane,max_circular)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends
