class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        fathers = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(i):
            if fathers[i] != i:
                fathers[i] = find(fathers[i])
            return fathers[i]
        
        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i == root_j:
                return False
            if rank[root_i] < rank[root_j]:
                root_i, root_j = root_j, root_i
            elif rank[root_i] == rank[root_j]:
                rank[root_i] += 1
            fathers[root_j] = root_i
            return True

        for edge in edges:
            if not union(*edge):
                return edge
