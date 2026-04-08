class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
            
            
        def bfs(x1, y1):
            q = deque()
            q.append((x1, y1, 0))
            visit = set()
            visit.add((x1, y1))

            while q:
                x2, y2, steps = q.popleft()
                if x2 == x and y2 == y:
                    return steps

                for dx, dy in directions:
                    nx, ny = x2 + dx, y2 + dy
                    if (nx, ny) in visit:
                        continue
                    visit.add((nx, ny))
                    q.append((nx, ny, steps + 1))
            return -1

        return bfs(0, 0)
