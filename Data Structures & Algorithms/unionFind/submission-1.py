class UnionFind:
    
    def __init__(self, n: int):
        self.rank  = [1] * n
        self.parent = [i for i in range(n)]
        self.n = n

    def find(self, x: int) -> int:
        # iterative approach
        # p = self.parent[x]
        # while p != self.parent[p]:
        #     self.parent[p] = self.parent[self.parent[p]]
        #     p = self.parent[p]
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
            
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)

        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
                self.rank[p1] += self.rank[p2]
            else:
                self.parent[p1] = p2
                self.rank[p2] += self.rank[p1]
            self.n-=1
            return True
        return False
        

    def getNumComponents(self) -> int:
        return self.n

