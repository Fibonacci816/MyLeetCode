class Solution:
    # 计算所有分数然后执行排序算法直到找到第k小的分数
    # 时间O(n^2*logn) 空间O(n^2)
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        fracs = {arr[i]/arr[j]: [arr[i], arr[j]] for i in range(n) for j in range(i+1, n)}
        def partition(arr, l, r):
            pivot = random.randint(l, r)
            pivot_val = arr[pivot]
            arr[l], arr[pivot] = arr[pivot], arr[l]
            idx = l
            for i in range(l+1, r+1):
                if arr[i] < pivot_val:
                    idx += 1
                    arr[idx], arr[i] = arr[i], arr[idx]
            arr[l], arr[idx] = arr[idx], arr[l]
            return idx
        
        def quick_sort(arr, l, r, k):
            pivot = partition(arr, l, r)
            if pivot == k:
                return arr[pivot]
            elif pivot < k:
                return quick_sort(arr, pivot+1, r, k)
            else:
                return quick_sort(arr, l, pivot-1, k)
            
        return fracs[quick_sort(list(fracs.keys()), 0, len(fracs)-1, k-1)]