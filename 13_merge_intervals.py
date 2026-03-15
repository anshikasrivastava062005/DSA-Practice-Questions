'''
Merge Intervals:
Problem: Given a collection of intervals, merge all overlapping intervals.
Input: Intervals: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Intervals [1,3] and [2,6] overlap, so they are merged into [1,6]. The others remain
unchanged.'''

intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()

merged = []

for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

print(merged)

