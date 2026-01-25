class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])

        count = 0
        last_end = intervals[0][1]

        for s, e in intervals[1:]:
            if s < last_end:
                count += 1   
            else:
                last_end = e 

        return count

        