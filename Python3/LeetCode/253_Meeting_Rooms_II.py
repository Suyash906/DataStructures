class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = []
        end = []
        
        for curr in intervals:
            start.append(curr[0])
            end.append(curr[1])
        
        start.sort()
        end.sort()
        
        size = len(intervals)
        
        rooms, e = 0, 0
        
        for s in range(size):
            if start[s] < end[e]:
                rooms += 1
            else:
                e += 1
                
        return rooms
