class Solution(object):
    # 快速排序
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def partition(l, r):
            pivot = random.randint(l, r)
            pivot_val = nums[pivot]
            nums[pivot], nums[l] = nums[l], nums[pivot]
            i = l
            for j in range(l+1, r+1):
                if nums[j] < pivot_val:  # '<' 也可以改为 '<='，但'<'可以减少交换次数
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[l] = nums[l], nums[i]
            return i
        
        def partition2(l, r):
            pivot = random.randint(l, r)
            pivot_val = nums[pivot]
            nums[pivot], nums[l] = nums[l], nums[pivot]  # 可以简化为nums[pivot] = nums[l]，因为nums[l]要被替换，所以l的位置是什么并没有影响
            while l < r:
                while l < r and nums[r] >= pivot_val:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] <= pivot_val:  # 上一个判断条件的'>='和这个判断条件的'<='，至少有一个带'='，否则会死循环；都带'='可以减少交换次数
                    l += 1
                nums[r] = nums[l]
            nums[l] = pivot_val
            return l 
        
        def quick_sort(l, r):
            pivot = partition2(l, r)
            if l < pivot - 1:
                quick_sort(l, pivot-1)
            if pivot + 1 < r:
                quick_sort(pivot+1, r)
        
        quick_sort(0, len(nums)-1)
        return nums


    # 归并排序（非递归）
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums1, nums2):
            n1 = len(nums1)
            n2 = len(nums2)
            res = []
            i = j = 0
            while i < n1 and j < n2:
                if nums1[i] < nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            if i < n1:
                res += nums1[i:]
            if j < n2:
                res += nums2[j:]
            return res
        
        d = 1
        n = len(nums)
        while d < n:
            d *= 2
            for i in range(0, n, d):
                nums[i:i+d] = merge(nums[i:i+d//2], nums[i+d//2:i+d])      
        return nums

    # 堆排序
    def sortArray(self, nums: List[int]) -> List[int]:
        def max_heapify(nums, root, l):
            while root * 2 + 1 < l:
                child = root * 2 + 1
                if child + 1 < l and nums[child+1] > nums[child]:
                    child += 1
                if nums[child] > nums[root]:
                    nums[child], nums[root] = nums[root], nums[child]
                    root = child
                else:
                    break
        
        def build_heap(nums):
            l = len(nums)
            for i in range(l//2, -1, -1):
                max_heapify(nums, i, l)

        def heap_sort(nums):
            build_heap(nums)
            for i in range(len(nums)-1, -1, -1):
                nums[i], nums[0] = nums[0], nums[i]
                max_heapify(nums, 0, i)

        heap_sort(nums)
        return nums
