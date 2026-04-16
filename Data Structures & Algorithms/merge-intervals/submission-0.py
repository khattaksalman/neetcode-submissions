class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        res = []
        new_intervals = intervals[0]
        for interval in range(1,len(intervals)):
            if intervals[interval][1] < new_intervals[0]:
                res.append(interval)

            elif intervals[interval][0] > new_intervals[1]:
                res.append(new_intervals)
                new_intervals=intervals[interval]

            else:
                new_intervals[0] = min(intervals[interval][0],new_intervals[0])
                new_intervals[1] = max(intervals[interval][1],new_intervals[1])

        res.append(new_intervals)                

        return res        
