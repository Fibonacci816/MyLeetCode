class Solution:
    # 时间O(N) 空间O(N)，其中N为正整数n的位数
    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))
        l = len(arr)
        MAX_INT = 2 ** 31 - 1
        for i in range(l-2, -1, -1):
            if arr[i] >= arr[i+1]:
                continue
            for j in range(l-1, i, -1):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    arr[i+1:l] = arr[i+1:l][::-1]
                    ans = int(''.join(arr))
                    return ans if ans <= MAX_INT  else -1
        return -1