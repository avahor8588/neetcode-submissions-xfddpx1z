class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visit = set()

        # Initialize queue with starting node and distance 0
        q = deque([(0, 0, 0)])  # (row, col, distance)
        visit.add((0, 0))

        while q:
            r, c, dist = q.popleft()

            # Check if we've reached the bottom-right corner
            if r == ROWS - 1 and c == COLS - 1:
                return dist

            # Explore neighbors
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (
                    0 <= row < ROWS
                    and 0 <= col < COLS
                    and (row, col) not in visit
                    and grid[row][col] == 0
                ):
                    visit.add((row, col))
                    q.append((row, col, dist + 1))  # Enqueue with updated distance

        # If no path exists
        return -1
