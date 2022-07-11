class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = dict(zip(order, range(len(order))))
        for i in range(1, len(words)):
            if [order_map[c] for c in words[i]] < [order_map[c] for c in words[i-1]]:
                return False
        return True
