class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 'L':
                grid[r][c] = 'W'

                dfs(r - 1, c)  # Up
                dfs(r + 1, c)  # Down
                dfs(r, c - 1)  # Left
                dfs(r, c + 1)  # Right

        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':
                    dfs(r, c)
                    island_count += 1

        return island_count
