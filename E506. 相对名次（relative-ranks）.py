class Solution:
    # 时间O(n) 空间O(n)
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_with_id = sorted(enumerate(score), key=lambda x: -x[1])
        res = [''] * len(score)
        top3 = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, (id, _) in enumerate(score_with_id):
            res[id] = top3[i] if i < 3 else str(i + 1)
        return res
