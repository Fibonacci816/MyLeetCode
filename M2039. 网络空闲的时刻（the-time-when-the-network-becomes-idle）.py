class Solution:
    # bfs
    # 时间O(n+m) 空间O(n+m)
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        links = defaultdict(list)
        for node1, node2 in edges:
            links[node1].append(node2)
            links[node2].append(node1)

        def get_time(tt, pat):
            rtt = 2 * tt
            # return (rtt - 1) // pat * pat + rtt
            time = rtt
            if rtt > pat:
                if rtt % pat == 0:
                    time += rtt - pat
                else:
                    time += rtt - rtt % pat
            return time
     
        def bfs():
            ans = 0
            visited = [0] * len(patience)
            que = deque([(0, 0)])
            visited[0] = 1
            while que:
                node, tt = que.popleft()
                tt += 1
                for next_node in links[node]:
                    if not visited[next_node]:
                        ans = max(ans, get_time(tt, patience[next_node]))
                        que.append((next_node, tt))
                        visited[next_node] = 1
            return ans + 1

        return bfs()
