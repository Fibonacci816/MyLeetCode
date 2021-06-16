class Solution(object):
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
                if nums[j] < pivot_val:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[l] = nums[l], nums[i]
            return i
        
        def partition2(l, r):
            pivot = random.randint(l, r)
            pivot_val = nums[pivot]
            nums[pivot], nums[l] = nums[l], nums[pivot]
            while l < r:
                while l < r and nums[r] >= pivot_val:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] <= pivot_val:
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