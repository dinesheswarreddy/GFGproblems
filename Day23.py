#Count Inversions
class Solution:
    def inversionCount(self, arr):
        def sort(arr, left, right):
            count = 0
            if left < right:
                mid = left + (right - left) // 2
                count += sort(arr, left, mid)
                count += sort(arr, mid + 1, right)
                count += merge(arr, left, mid, right)
            return count

        def merge(arr, left, mid, right):
            inversion = 0
            size1 = mid - left + 1
            size2 = right - mid
            leftArr = arr[left:left + size1]
            rightArr = arr[mid + 1:mid + 1 + size2]
            i = j = 0
            k = left
            while i < size1 and j < size2:
                if leftArr[i] <= rightArr[j]:
                    arr[k] = leftArr[i]
                    i += 1
                else:
                    arr[k] = rightArr[j]
                    j += 1
                    inversion += (mid + 1) - (left + i)
                k += 1
            while i < size1:
                arr[k] = leftArr[i]
                i += 1
                k += 1
            while j < size2:
                arr[k] = rightArr[j]
                j += 1
                k += 1
            return inversion

        return sort(arr, 0, len(arr) - 1)
solution = Solution()
arr = [38, 27, 43, 3, 9, 82, 10]
count = solution.inversionCount(arr)
print(count)  # Output: 11 (the inversion count)
print(arr)  # Sorted array after the count
