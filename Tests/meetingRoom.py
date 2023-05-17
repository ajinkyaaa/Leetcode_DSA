"""
intervals = [[0,30],[10,40],[50,60],[45,90]]

[[0,30],[10,40],[45,90],[50,60]]

use case:-
intervals start and end where end > start
find no of rooms required and any given point ofmtime

result:-
[0,30]

[0,30][10,40] since starttime of 2nd is less than end time

[45,90] pop 1 

[45,90][50,60]


"""

import heapq
def minMeetingRooms(intervals):
    meetingRooms = []
    intervals.sort(key = lambda x:x[0])
    heapq.heappush(meetingRooms,intervals[0][1])
    for i in intervals[1:]:
        if len(meetingRooms) == 0:
            heapq.heappush(i[0][1])
            
        else:
            endTime = heapq.heappop(meetingRooms)
            if i[0]<endTime:
                heapq.heappush(meetingRooms,i[0])
                heapq.heappush(meetingRooms,endTime)
            else:
                heapq.heappush(meetingRooms,i[0])

    return len(meetingRooms)

a=minMeetingRooms([[0,30],[10,40],[50,60],[45,90]])

assert minMeetingRooms([[0,30],[10,40],[50,60],[45,90]]) == 2
assert minMeetingRooms([[0,30],[30,40],[50,60],[60,90]]) == 1
assert minMeetingRooms([[0,100],[30,40],[50,60],[60,90]]) == 2 




