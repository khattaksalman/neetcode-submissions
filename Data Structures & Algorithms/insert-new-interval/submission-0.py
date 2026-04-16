class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)

    # case 2: interval completely after newInterval
            elif interval[0] > newInterval[1]:
              res.append(newInterval)
              newInterval = interval

    # case 3: overlap → merge
            else:
              newInterval[0] = min(interval[0], newInterval[0])
              newInterval[1] = max(interval[1], newInterval[1])


        res.append(newInterval)       
        
        return res
        