class Graph:
    
    def __init__(self):
        self.adj = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()
        
        self.adj[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adj and dst in self.adj[src]:
            self.adj[src].remove(dst)
            return True
        return False
                    


    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj:
            return False
        visit = set()
        def dfs(node):
            if node == dst:
                return True
            if node in visit:
                return False
            
            for nie in self.adj.get(node, set()):
                if dfs(nie):
                    return True
                
            return False
        return dfs(src)
            



