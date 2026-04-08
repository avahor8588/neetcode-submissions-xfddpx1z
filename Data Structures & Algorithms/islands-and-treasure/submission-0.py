class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dist = 0

        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                if (r,c) in visit:
                    continue
                
                visit.add((r,c))
                grid[r][c] = dist

                for dr,dc in moves:
                    row = r+dr
                    col = c+dc
                    if (row<0 or row>= ROWS or col <0 or col >= COLS or grid[row][col] == -1):
                        continue

                    q.append((row,col))
            dist+=1 
