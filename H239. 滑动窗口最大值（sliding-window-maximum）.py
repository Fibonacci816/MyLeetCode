class Solution:
    # 最大堆 O(nlogn)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-nums[i], i)for i in range(k)]
        heapify(q)
        res = [-q[0][0]]
        for i in range(k, len(nums)):
            heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heappop(q)
            res.append(-q[0][0])
        return res

    # 双向单调队列
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i < k-1: continue
            while q[0] <= i - k:
                q.popleft()
            res.append(nums[q[0]])
        return res
