class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for src, dest, weight in edges:
            adj[src].append([weight, dest])
            adj[dest].append([weight, src])

        visit = set()
        minH = [[0, 0]]  # [weight, node]
        res = 0
        while minH and len(visit) < n:
            weight, node = heapq.heappop(minH)
            if node in visit:
                continue
            visit.add(node)
            res += weight
            for w, neighbor in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(minH, [w, neighbor])
        return res if len(visit) == n else -1