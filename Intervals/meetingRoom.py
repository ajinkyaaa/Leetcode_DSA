import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        
        if not intervals:
            return 0

        free_rooms = []

        intervals.sort(key= lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:

            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)



import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetingRooms = []
        intervals.sort(key = lambda x:x[0]) # sort based on start time
        #[[0,30],[5,10],[15,20]]
        for i in intervals:
            start, end = i[0],i[1]
            if len(meetingRooms) == 0:
                heapq.heappush(meetingRooms,end) # [0,30]
            
            else:
                lastEndTime = heapq.heappop(meetingRooms) #30
                if start < lastEndTime:
                    heapq.heappush(meetingRooms,end) # [10]
                    heapq.heappush(meetingRooms,lastEndTime) # [10,30]
                else:
                    heapq.heappush(meetingRooms,end) #[10]

        return len(meetingRooms)

"""
#steps:-
sort by start time 

if starttime is greater than endtime of heap, pop from heap
add to heap

"""