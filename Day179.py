#Meeting Rooms III
from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        ongoing_meetings = []  # (end_time, room)
        meeting_count = [0] * n

        for start, end in meetings:
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
            else:
                earliest_end, room = heapq.heappop(ongoing_meetings)
                duration = end - start
                new_end = earliest_end + duration
                heapq.heappush(ongoing_meetings, (new_end, room))

            meeting_count[room] += 1

        max_meetings = max(meeting_count)
        for i, count in enumerate(meeting_count):
            if count == max_meetings:
                return i


if __name__ == "__main__":
    sol = Solution()

    # ✅ Inbuilt Example
    n1 = 2
    meetings1 = [[0, 6], [2, 3], [3, 7], [4, 8], [6, 8]]
    print("Inbuilt Example Output:", sol.mostBooked(n1, meetings1))  # Expected: 1

    # 🧑‍💻 User Input
    print("\nNow enter your own input:")
    n = int(input("Enter number of rooms (n): "))
    m = int(input("Enter number of meetings: "))
    meetings = []
    print("Enter meetings as 'start end' (without quotes):")
    for _ in range(m):
        s, e = map(int, input().split())
        meetings.append([s, e])
    
    result = sol.mostBooked(n, meetings)
    print("Room with most meetings:", result)
