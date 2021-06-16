class Solution(object):
    # 堆排序
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        heap = [] #创建了一个空堆
        heappush(heap,item) #往堆中插入一条新的值
        item = heappop(heap) #从堆中弹出最小值
        item = heap[0] #查看堆中最小值，不弹出
        heapify(x) #以线性时间讲一个列表转化为堆
        item = heapreplace(heap,item) #弹出并返回最小值，然后将heapqreplace方法中item的值插入到堆中，堆的整体结构不会发生改变。
        heappushpop() #顾名思义，将值插入到堆中同时弹出堆中的最小值。
        merge(*iterables) #合并多个堆然后输出
        """
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

    # 快速排序
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def partition(l, r):
            pivot = random.randint(l, r)
            pivot_val = nums[pivot]
            nums[l], nums[pivot] = nums[pivot], nums[l]
            while l < r:
                while l < r and nums[r] >= pivot_val:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] <= pivot_val:
                    l += 1
                nums[r] = nums[l]
            nums[l] = pivot_val
            return l

        def partition2(l, r):
            pivot = random.randint(l, r)
            pivot_val = nums[pivot]
            nums[l], nums[pivot] = nums[pivot], nums[l]
            i = l
            for j in range(l+1, r+1):
                if nums[j] < pivot_val:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            return i

        def quick_sort(l, r):
            pivot = partition2(l, r)
            if pivot == n - k:
                return nums[pivot]
            if pivot < n - k: 
                return quick_sort(pivot+1, r)
            else:
                return quick_sort(l, pivot-1)
        
        return quick_sort(0, n-1)

        # 自建堆，排序过程中返回目标
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        def heappy(i, max_size):
            parent = i
            while 2 * parent + 1 < max_size:
                child = 2 * parent + 1
                if child < max_size - 1 and nums[child] < nums[child+1]:
                    child += 1
                if nums[parent] < nums[child]:
                    nums[parent], nums[child] = nums[child], nums[parent]
                    parent = child
                else:
                    break
        
        def build_heap(nums, max_size):
            for i in range(max_size // 2, -1, -1):
                heappy(i, max_size)
        
        def heap_sort(nums, max_size, k):
            build_heap(nums, max_size)
            for i in range(max_size-1, -1, -1):
                if i == k:
                    return nums[0]
                nums[i], nums[0] = nums[0], nums[i]
                heappy(0, i)
                
        max_size = len(nums)
        return heap_sort(nums, max_size, max_size-k)
