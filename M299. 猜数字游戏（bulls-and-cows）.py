class Solution:
    # 遍历+hash（遍历过程中统计公牛，并记录字符数量，最后统计重叠的字符个数即为奶牛）
    # 时间O(n) 空间O(k)（k为不同字符的个数）
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        # 由于本题中字符为0-9，所以可以用长度为10的数组代替dict
        secret_dict = defaultdict(int)
        guess_dict = defaultdict(int)
        bulls = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_dict[secret[i]] += 1
                guess_dict[guess[i]] += 1
        cows = sum(min(v, guess_dict[k]) for k, v in secret_dict.items())
        return f"{bulls}A{cows}B"
