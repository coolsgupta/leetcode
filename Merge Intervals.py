class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])
        new_intervals = []

        i = 0

        while (i < len(intervals)):
            s, e = intervals[i]
            i += 1
            while (i < len(intervals)):
                s_c, e_c = intervals[i]
                if e >= s_c:
                    e = max(e_c, e)
                    s_c, e_c = intervals[i]
                    i += 1
                else:
                    break

            new_intervals.append([s, e])

        return new_intervals

