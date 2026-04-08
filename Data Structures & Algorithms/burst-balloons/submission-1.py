class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums+[1]
        dp = {}
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            #stimulates the branches of the 
            dp[(l, r)] = 0
            for i in range(l, r + 1):  # Try popping each balloon last in the range [l, r]
                # Calculate the coins obtained by popping balloon i last
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                # Add coins obtained from left and right subproblems
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)  # Update the maximum coins for range [l, r]

            return dp[(l,r)]
        
        return dfs(1, len(nums)-2)
                

            
