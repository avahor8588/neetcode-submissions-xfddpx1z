class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        dp = {}
        def dfs(i, cap):
            if i >= len(profit):
                return 0
            if (i, cap) in dp :
                return dp[(i,cap)]
            
            skip = dfs(i+1, cap)

            include = 0
            if cap - weight[i] >= 0:
                include = profit[i] + dfs(i, cap - weight[i])
            dp[(i, cap)] = max(skip,include)
            return dp[(i, cap)]

        return dfs(0,capacity) 
            


            

            

