class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    # 根据极坐标公式（(x-x_c)^2 + (y-y_c)^2 = ρ^2）求x和y
    def randPoint(self) -> List[float]:
    	# 这一步是关键，必须对均匀分布生成的随机数开方，原因如下：
    	# 设生成的随机数为ra，那么需要生成的圆的面积为ra * S，其中S=π*radius^2，
    	# 只有这样才能满足均匀分布，即落入某区域的概率等于某区域的面积占比
        r = self.radius * math.sqrt(random.random())
        # sita = random.uniform(0, 2 * math.pi)
        sita = 2 * math.pi * random.random()
        return [self.x_center + r * math.cos(sita), self.y_center + r * math.sin(sita)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()