#Non-overlapping Intervals

class Solution:
    def minRemoval(self, intervals):
        # Code here
        if not intervals:
            return 0
    
        intervals.sort(key=lambda x: x[1])
    
        last_end = float('-inf')
        remove_count = 0
    
        for interval in intervals:
            if interval[0] < last_end:
                remove_count += 1
            else:
                last_end = interval[1]
    
        return remove_count


if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
