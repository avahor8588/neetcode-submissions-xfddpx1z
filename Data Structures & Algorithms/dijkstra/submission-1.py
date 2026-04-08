class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = collections.defaultdict(list)
        for s, d, w in edges:
            adj[s].append((w, d))
        
        # Min-heap to store the (current_weight, node) pairs
        minh = [(0, src)]
        visit = {i: -1 for i in range(n)}  # Initialize all distances as -1

        while minh:
            weight, node = heapq.heappop(minh)
            
            # Skip if already visited with a shorter path
            if visit[node] != -1:
                continue

            visit[node] = weight  # Set the shortest path to this node

            for w2, n2 in adj[node]:
                if visit[n2] == -1:  # Only push unvisited nodes
                    heapq.heappush(minh, (weight + w2, n2))
        
        # Ensure source node's distance is set to 0
        visit[src] = 0
        return visit