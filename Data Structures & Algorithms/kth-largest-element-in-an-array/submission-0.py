class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        we can have a count of up to nums items
        """
        temp = []
        for n in nums:
            heapq.heappush(temp, n*-1)
        
        res = 0
        for i in range(k):
            res = heapq.heappop(temp) * -1
        return res
        