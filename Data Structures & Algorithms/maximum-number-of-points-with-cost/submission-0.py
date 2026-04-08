class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        dp ={}
        def dfs(r,c):
            if r==ROWS-1:
                return points[r][c]
            if(r,c) in dp:
                return dp[(r,c)]
            
            temp = float("-inf")
            for i in range(COLS):
                temp = max(temp, points[r][c]+ dfs(r+1,i)- abs(i-c))
            dp[(r,c)]= temp
            return temp
        res = float(("-inf"))
        for i in range(COLS):
            res = max(res,dfs(0,i))
        return res
                    
        