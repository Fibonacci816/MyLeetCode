class Solution(object):
    def __init__(self):
        self.mem = {}
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (word1, word2) in self.mem:
            return self.mem[(word1, word2)]
        res = None
        if len(word1) == 0:
            res = len(word2)
        elif len(word2) == 0:
            res = len(word1)
        elif word1[0] == word2[0]:
            res = self.minDistance(word1[1:], word2[1:])
        else:
            res = 1 + min(
                self.minDistance(word1, word2[1:]),
                self.minDistance(word1[1:], word2[1:]),
                self.minDistance(word1[1:], word2)
                )
        self.mem[(word1, word2)] = res
        return res