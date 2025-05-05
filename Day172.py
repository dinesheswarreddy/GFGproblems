#Search in an almost Sorted Array

class Solution:
    def findTarget(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            if mid > low and arr[mid - 1] == target:
                return mid - 1
            if mid < high and arr[mid + 1] == target:
                return mid + 1

            if arr[mid] > target:
                high = mid - 2
            else:
                low = mid + 2

        return -1


# --------------------------
# 🔧 Example Usage Section
# --------------------------

if __name__ == "__main__":
    s = Solution()

    # 🔹 Built-in Test Case
    arr1 = [10, 3, 40, 20, 50, 80, 70]
    target1 = 40
    print("Built-in Test Case:")
    print(f"Input: arr = {arr1}, target = {target1}")
    print("Output:", s.findTarget(arr1, target1))
    print()

    # 🔹 User Input Test Case
    print("User Input Test Case:")
    arr_input = input("Enter array elements (space-separated): ").strip()
    arr2 = list(map(int, arr_input.split()))
    target2 = int(input("Enter target value: "))
    print("Output:", s.findTarget(arr2, target2))
