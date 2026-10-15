from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]


        max_island_size = 0

        for i in range(n): 
            for j in range(m): 
                if grid[i][j] == 0: 
                    continue
                if visited[i][j]: 
                    continue
                

                q = deque()

                q.append((i, j))
                visited[i][j] = True
                island_size = 1

                while len(q) > 0: 
                    x, y = q.popleft()
                    for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]: 
                        if new_x < 0 or new_x >= n: 
                            continue
                        if new_y < 0 or new_y >= m: 
                            continue
                        if visited[new_x][new_y]: 
                            continue
                        if grid[new_x][new_y] == 0: 
                            continue
                        visited[new_x][new_y] = True
                        q.append((new_x, new_y))
                        island_size += 1

                max_island_size = max(max_island_size, island_size)




        return max_island_size





