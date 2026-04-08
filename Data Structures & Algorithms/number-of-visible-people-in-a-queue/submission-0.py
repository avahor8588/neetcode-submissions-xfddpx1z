class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        """
        i see it now

        so we want to keep in our stack the max value to the right of it ever
        -> so what we would do is chekc if curr > stack[-1], if it is we can pop
        """
        stack= []
        res = [0] * len(heights)
        for i in range(len(heights)-1, -1,-1):
            n = heights[i]
            while stack and stack[-1] < n:
                #basically pop eveyrhting we can see
                stack.pop()
                res[i]+=1
            if stack : #we see the largest value to the right of 
                res[i]+=1
            stack.append(n)
        return res