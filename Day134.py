#Activity Selection

class Solution:
    def activitySelection(self, start, finish):
        n = len(start)
        if n == 0:
            return 0
        
        # Pair each activity's finish time with its start time
        activities = list(zip(finish, start))
        
        # Sort activities based on finish times
        activities.sort()
        
        count = 1
        last_finish = activities[0][0]
        
        for i in range(1, n):
            current_start = activities[i][1]
            if current_start > last_finish:
                count += 1
                last_finish = activities[i][0]
        
        return count

# Example Usage 1: User input
start = list(map(int, input("Enter the start times of activities (space-separated): ").split()))
finish = list(map(int, input("Enter the finish times of activities (space-separated): ").split()))

sol = Solution()
print("Maximum number of activities that can be selected:", sol.activitySelection(start, finish))

# Example Usage 2: Inbuilt input
start_example = [1, 3, 0, 5, 8, 5]
finish_example = [2, 4, 6, 7, 9, 9]

print("Maximum number of activities that can be selected for inbuilt example:", sol.activitySelection(start_example, finish_example))
