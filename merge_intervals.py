def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for inter in intervals[1:]:
        last_merged = merged[-1]

        if inter[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], inter[1])
        else:
            merged.append(inter)
    return merged
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))

