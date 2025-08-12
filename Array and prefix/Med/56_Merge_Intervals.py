'''56. Merge Intervals'''

'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping 
intervals, and return 
an array of the non-overlapping intervals that cover all the intervals in the input.'''
# brute fprce
class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        # Make a copy to avoid modifying the original list
        intervals = [interval[:] for interval in intervals]
        merged = True
        
        # Continue until no more merges happen
        while merged:
            merged = False
            i = 0
            while i < len(intervals):
                j = i + 1
                while j < len(intervals):
                    # Check if intervals[i] and intervals[j] overlap
                    if (intervals[i][0] <= intervals[j][1] and 
                        intervals[j][0] <= intervals[i][1]):
                        # Merge them
                        intervals[i][0] = min(intervals[i][0], intervals[j][0])
                        intervals[i][1] = max(intervals[i][1], intervals[j][1])
                        # Remove the merged interval
                        intervals.pop(j)
                        merged = True
                    else:
                        j += 1
                i += 1
        
        return intervals
    


# optimal
class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        # Sort the intervals based on the start value
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                # There is overlap, merge them
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        
        return merged