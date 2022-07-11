class Solution:
    # 排序 匹配
    # 时间O(nlogn) 空间O(n)
    def canReorderDoubled(self, arr: List[int]) -> bool:
        pos_arr, neg_arr = [], []
        n_pos = n_neg = 0
        for num in arr:
            if num > 0:
                pos_arr.append(num)
                n_pos += 1
            elif num < 0:
                neg_arr.append(-num)
                n_neg += 1
        if n_pos % 2 != 0 or n_neg % 2 != 0:
            return False
        
        def is_double(arr, n):
            arr.sort()
            matched = [0] * n
            j = 0
            # 两层循环但j递增，因此时间复杂度O(n)
            for i in range(n):
                if matched[i]:
                    continue
                while j < n - 1:
                    j += 1
                    if not matched[j] and arr[j] == 2 * arr[i]:
                        matched[i] = matched[j] = 1
                        break
                if not matched[i]:
                    return False
            return True

        return is_double(pos_arr, n_pos) and is_double(neg_arr, n_neg)
    
    # 计数+排序 匹配
    # 时间O(nlogn) 空间O(n)
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        if cnt[0] % 2:
            return False
        for num in sorted(cnt, key=abs):
            if cnt[num] > cnt[2 * num]:
                return False
            cnt[2 * num] -= cnt[num]
        return True