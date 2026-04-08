class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        #rows ->items
        #cols capacity
        N, M = len(profit), capacity
        dp = [[0] * (M + 1) for _ in range(N)]
        
        #pre work
        # we want to intialize all items with a capcity of 0
        #because with a capacity fo 0 we cant collect any profit ?
        
        # intialize the first entire row of cols
        for c in range(M + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0]
        
        # we already filled the filled the grid first row and col
        for i in range(1,N):
            for c in range(1,M+1):
                #choice to skip so pick the previous row and capcity
                # so esentially previous item at same caacity
                skip = dp[i-1][c]
                include = 0
                if c- weight[i] >=0:
                    include = profit[i] + dp[i-1][c-weight[i]]

                dp[i][c] = max(include, skip)



        return dp[N-1][M]
                


        
