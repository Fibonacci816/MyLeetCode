class Solution:
    # 二分查找
    # 时间O(logn)（最差O(n)） 空间O(1)
    def search(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                if arr[0] == target:
                    return 0
                while mid > 0 and arr[mid] == arr[mid-1]:
                    mid -= 1
                return mid
            while l < mid and arr[l] == arr[mid]:
                l += 1
            while r > mid and arr[r] == arr[mid]:
                r -= 1
            if arr[l] <= arr[mid]:
                if arr[l] <= target < arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if arr[mid] < target <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
