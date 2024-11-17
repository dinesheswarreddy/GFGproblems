#Today's Problems: 
#1️⃣ Second Largest Element 
class Solution:
    def getSecondLargest(self, arr):
        first = second = -1
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
        
        return second if second != -1 else -1
#2️⃣ Move All Zeroes to End
class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	lastNonZeroFoundAt = 0 
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[lastNonZeroFoundAt], arr[i] = arr[i], arr[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1

