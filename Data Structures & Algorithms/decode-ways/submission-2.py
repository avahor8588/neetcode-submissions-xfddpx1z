class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in dp:
                return dp[i]
            
            if s[i] == '0':
                return 0
            
            # number of different ways
            full = 0
            if i < len(s)-1:
                #second chracter
                if (s[i] == "1") or (s[i] == "2" and s[i+1]  <"7"):
                    full = dfs(i+2)
            
            single = dfs(i+1)

            dp[i] = full+single
            return dp[i]
        return dfs(0)