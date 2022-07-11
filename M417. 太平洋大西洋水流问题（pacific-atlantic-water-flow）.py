class Solution:
    # bfs(或dfs)
    # 时间O(mn) 空间O(mn)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def bfs(start):
            visited = set(start)
            que = deque(start)
            while que:
                x, y = que.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and heights[new_x][new_y] >= heights[x][y]:
                        visited.add((new_x, new_y))
                        que.append((new_x, new_y))
            return visited
        
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(m)]
        atlantic = [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m)]
        return [[x, y] for x, y in bfs(pacific) & bfs(atlantic)]