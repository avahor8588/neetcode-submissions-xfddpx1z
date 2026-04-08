class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
        
        visit = set()
        cycle = set()
        res = []
        
        def dfs(node):
            if node in visit:
                return True
            if node in cycle:
                return False
            cycle.add(node)
            for nie in adj[node]:
                if not dfs(nie):
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        for i in range(n):
            if i not in visit and not dfs(i):
                return []  # Return empty if a cycle is detected

        return res[::-1] 