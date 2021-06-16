class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 自定义比较运算
        def cmp(str1, str2):
            return (0 if str1+str2 == str2+str1 else 
            1 if str1+str2 > str2+str1 else -1)

        nums_str = [str(num) for num in nums]
        nums_str.sort(key=functools.cmp_to_key(cmp), reverse=True)
        res = ''.join(nums_str)
        for i in range(len(res)):
            if res[i] != '0':
                break
        return res[i:]