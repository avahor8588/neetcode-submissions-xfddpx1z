class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        must be shiped from one port to another within days
        each idx has a weight of weight[i]

        binary search
        -> low would be max of nums
        -> high would be sum(nums)

        now lets go ahead and do this and use buckets here
        so lets first go and use the mid
        -> add numbers until one number gets too lareg then start anothrt
        -> if our count is greater then days break out of that 
        -> if it is not and window = days then we can return the m
        the cpapcaity

        -> if our windoes is greater then 4 then we incease our lwot to m +1
        -> if our windoes is smaller than days then we have to  decrease m
        """
        l = max(weights)
        h = sum(weights)
        while l <h:
            m = (l + h) // 2

            total = 0
            count =1 
            for i in range(len(weights)):
                w = weights[i]

                if total + w > m :
                    total = 0
                    count += 1
                if count > days:
                    break

                total+= weights[i]
            if count > days:
                l= m+1
            else:
                h = m
        return l
        







