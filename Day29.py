#Sorted and Rotated Minimum
class Solution:
    def findMin(self, arr):
        #complete the function 
        mini=float('inf')
        for i in range(0,len(arr)):
                if arr[i]<=mini:
                    mini=arr[i]
        return mini
