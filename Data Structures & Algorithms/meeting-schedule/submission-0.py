"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
       
        for i in range(1,len(intervals)):
            s1 = intervals[i].start
            e2 = intervals[i-1].end-1

            if s1 <= e2:
                return  False

        return True        