#Maximum Product Subarray

class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		max_prod = min_prod = result = arr[0]
    
        for i in range(1, len(arr)):
            if arr[i] < 0:
                max_prod, min_prod = min_prod, max_prod
        
            max_prod = max(arr[i], max_prod * arr[i])
            min_prod = min(arr[i], min_prod * arr[i])
        
            result = max(result, max_prod)
    
        return result
