#Overlapping Intervals
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort the intervals by the starting time
    intervals.sort(key=lambda x: x[0])
    
    # Initialize the list to store merged intervals
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        # Get the current interval and the last merged interval
        current = intervals[i]
        last_merged = merged[-1]
        
        # Check if the current interval overlaps with the last merged one
        if current[0] <= last_merged[1]:
            # Merge the intervals by updating the end time of the last merged interval
            merged[-1][1] = max(last_merged[1], current[1])
        else:
            # No overlap, add the current interval to merged list
            merged.append(current)
    
    return merged

# Example usage:
arr1 = [[1, 3], [2, 4], [6, 8], [9, 10]]
arr2 = [[6, 8], [1, 9], [2, 4], [4, 7]]

print(merge_intervals(arr1))  # Output: [[1, 4], [6, 8], [9, 10]]
print(merge_intervals(arr2))  # Output: [[1, 9]]
