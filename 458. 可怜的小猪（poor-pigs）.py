class Solution:
    # 信息论：nlog(k+1) >= log(buckets)  ->  n >= ceil(log(buckets)/log(k+1))小猪携带的信息>=毒药携带的信息，n为小猪数量，k为实验轮数
    # 每个小猪可以确定一个维度(k+1)个取值，(k+1)^n >= buckets  ->  n >= ceil(log(buckets)/log(k+1))
    # 时间O(1) 空间O(1)
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        k = minutesToTest // minutesToDie
        return ceil(log(buckets) / log(k+1))