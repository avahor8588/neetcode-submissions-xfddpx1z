class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r,c):
            if r<0 or r>= ROWS or c<0 or c>=COLS or (r,c) in visit or grid[r][c] ==1:
                return 0
            if r == ROWS -1 and c== COLS-1:
                return 1
            
            visit.add((r,c))
            res = dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)
            visit.remove((r,c))
            return res
        return dfs(0,0)
            
    