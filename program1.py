class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W' or (r, c) in visited:
                return
            
            visited.add((r, c))
            
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and (r, c) not in visited:
                    dfs(r, c)  
                    island_count += 1  
                    
        return island_count