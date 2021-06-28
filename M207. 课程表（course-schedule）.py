class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = defaultdict(int)
        links = defaultdict(list)
        zero_degree = {i for i in range(numCourses)}
        for pre, next in prerequisites:
            links[pre].append(next)
            indegrees[next] += 1
            zero_degree.discard(next)
        cnt = 0  # 已学习课程数量
        while zero_degree:
            course = zero_degree.pop()
            cnt += 1
            for next in links[course]:
                indegrees[next] -= 1
                if indegrees[next] == 0:
                    zero_degree.add(next)
        return cnt == numCourses
