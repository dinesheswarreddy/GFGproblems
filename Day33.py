#Aggressive Cows

def is_feasible(stalls, k, min_distance):
    # Greedily check if we can place k cows with at least `min_distance` apart
    count = 1  # Place the first cow in the first stall
    last_position = stalls[0]  # First cow is placed at the first stall
    
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_distance:
            count += 1
            last_position = stalls[i]
            if count == k:
                return True
    return False

def aggressiveCows(stalls, k):
    stalls.sort()  # Sort the stalls in ascending order
    low, high = 1, stalls[-1] - stalls[0]  # Binary search bounds
    
    best_dist = -1
    
    while low <= high:
        mid = (low + high) // 2
        if is_feasible(stalls, k, mid):
            best_dist = mid  # `mid` is a feasible solution, try for a larger distance
            low = mid + 1
        else:
            high = mid - 1  # `mid` is not feasible, try smaller distances
    
    return best_dist

# Example cases
print(aggressiveCows([1, 2, 4, 8, 9], 3))  # Output: 3
print(aggressiveCows([10, 1, 2, 7, 5], 3))  # Output: 4
print(aggressiveCows([2, 12, 11, 3, 26, 7], 5))  # Output: 1
