# 3. Reverse an Array
class Solution:
    def reverseArray(self, arr):
        # code here
        start, end = 0, len(arr)-1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

        return arr
