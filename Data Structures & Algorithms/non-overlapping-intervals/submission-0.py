class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        # finds longest path of non opverlapping interval
        dp ={}
        def dfs(i,prev):
            if i == len(intervals):
                return 0
            
            if (i,prev) in dp:
                return dp[(i,prev)]
            
            skip = dfs(i+1, prev)

            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                skip = max(skip,1+ dfs(i+1, i))
            
            dp[(i,prev)] = skip
            return dp[(i,prev)]
        
        return len(intervals) - dfs(0,-1)