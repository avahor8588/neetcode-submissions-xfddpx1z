class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = collections.defaultdict(list)
        for s,d,w in edges:
            adj[s].append([w,d])
        
        minH = [[0,src]]
        res = {}
        while minH:
            w, node = heapq.heappop(minH)
            if node in res:
                continue
            
            res[node] = w

            for w2,d in adj[node]:
                if d not in res:
                    heapq.heappush(minH, [w+w2, d])
        res[src] = 0
        for i in range(n):
            if i not in res:
                res[i]= -1
        return res
