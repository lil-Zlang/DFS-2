from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # found an island part
                    count += 1         # new island encountered
                    queue = deque([(r, c)])
                    grid[r][c] = '0'   # mark as visited

                    # BFS to mark all adjacent land parts as visited
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                queue.append((nr, nc))
                                grid[nr][nc] = '0'
        return count
