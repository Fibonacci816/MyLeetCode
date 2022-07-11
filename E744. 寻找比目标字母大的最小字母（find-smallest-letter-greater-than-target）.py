class Solution:
    # 时间O(n) 空间O(1)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        for c in letters:
            if c > target:
                return c

    # 时间O(logn) 空间O(1)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[0] if target >= letters[-1] else letters[bisect_right(letters, target)]