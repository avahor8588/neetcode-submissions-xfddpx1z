class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]  # Fix indexing
        self.rank = [1] * n
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

    def find(self, x):
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minH = []
        for src, dst, w in edges:
            heapq.heappush(minH, [w, src - 1, dst - 1])  # Convert to 0-based
        
        u_f = UnionFind(n)
        components = n
        res = 0

        while components > 1 and minH:
            w, n1, n2 = heapq.heappop(minH)

            if not u_f.union(n1, n2):
                continue
            res += w  # Fix typo here
            components -= 1

        return res if components == 1 else -1