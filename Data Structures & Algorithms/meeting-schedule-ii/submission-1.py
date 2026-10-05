"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        result = 0
        start_time = [i.start for i in intervals]
        end_time = [j.end for j in intervals]
        start_time.sort()
        end_time.sort()
        s,e = 0,0
        count = 0
        for _ in range(len(intervals)):
            if start_time[s] < end_time[e]:
                s+=1
                count+=1

            else:   
                e+=1
                count-=1
            result = max(result,count)
        return result