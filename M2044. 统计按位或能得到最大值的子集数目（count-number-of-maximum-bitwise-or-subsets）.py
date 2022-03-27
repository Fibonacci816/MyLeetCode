class Solution:
    # 遍历子集，计算子集按位或的值
    # 时间O(n·2^n) 空间O(n·2^n)
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def bitwise_or(nums):
            _or = 0
            for num in nums:
                _or |= num
            return _or
        
        sub_set = [[]]
        max_or = 0
        ans = 0
        for num in nums:
            new_eles = []
            for ele in sub_set:
                new_ele = ele + [num]
                _or = bitwise_or(new_ele)
                if _or > max_or:
                    max_or = _or
                    ans = 1
                elif _or == max_or:
                    ans += 1
                new_eles.append(new_ele)
            sub_set.extend(new_eles)
        return ans

    # 空间优化
    # 时间O(n·2^n) 空间O(1)
    def countMaxOrSubsets(self, nums: List[int]) -> int:  
        maxOr, cnt = 0, 0
        for i in range(1, 1 << len(nums)):
            orVal = reduce(or_, [num for j, num in enumerate(nums) if (i >> j) & 1], 0)
            if orVal > maxOr:
                maxOr, cnt = orVal, 1
            elif orVal == maxOr:
                cnt += 1
        return cnt


    # 时间优化，额外记录每个子集按位或的结果
    # 时间O(2^n) 空间O(n·2^n)（常数项为2）
    def countMaxOrSubsets(self, nums: List[int]) -> int:  
        sub_set = [([], 0)]
        max_or = 0
        ans = 0
        for num in nums:
            new_eles = []
            for ele, _or in sub_set:
                new_ele = ele + [num]
                _or |= num
                if _or > max_or:
                    max_or = _or
                    ans = 1
                elif _or == max_or:
                    ans += 1
                new_eles.append((new_ele, _or))
            sub_set.extend(new_eles)
        return ans

    # dfs回溯
    # 时间O(2^n) 空间O(n)
    def countMaxOrSubsets(self, nums: List[int]) -> int:  
        maxOr, cnt = 0, 0
        def dfs(pos: int, orVal: int) -> None:
            """
            pos 表示当前下标，orVal 表示当前下标之前的某个子集按位或值
            """
            if pos == len(nums):
                nonlocal maxOr, cnt
                if orVal > maxOr:
                    maxOr, cnt = orVal, 1
                elif orVal == maxOr:
                    cnt += 1
                return
            dfs(pos + 1, orVal | nums[pos])
            dfs(pos + 1, orVal)
        dfs(0, 0)
        return cnt
