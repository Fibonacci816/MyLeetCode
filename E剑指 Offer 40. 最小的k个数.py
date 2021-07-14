class Solution:
	# 借助堆
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for num in arr:
            heappush(heap, -num)
            if len(heap) > k:
                heappop(heap)
        res = [-num for num in heap]
        return res

    # 借助快排思想
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(arr, l, r):
            pivot_key = random.randint(l, r-1)
            pivot = arr[pivot_key]
            arr[pivot_key], arr[l] = arr[l], arr[pivot_key]
            idx = l
            for i in range(l, r):
                if arr[i] < pivot:
                    idx += 1
                    arr[idx], arr[i] = arr[i], arr[idx]
            arr[idx], arr[l] = arr[l], arr[idx]
            return idx
        
        def get_k_min(arr, l, r, k):
            pivot_key = partition(arr, l, r)
            if pivot_key == k - 1:
                return arr[:k]
            return get_k_min(arr, l, pivot_key, k) if k - 1 < pivot_key else get_k_min(arr, pivot_key+1, r, k)
        
        return [] if k <= 0 else get_k_min(arr, 0, len(arr), k)