class Solution:
	# dp 思路和回溯法类似
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(candidates)):
            num = candidates[i]
            if num == target:
                res.append([num]) 
            elif num < target:
                res.extend(sorted([num] + combination) for combination in self.combinationSum(candidates[i:], target-num)) 
        return res
