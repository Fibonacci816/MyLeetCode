class Solution:
    # 循环模拟
    # 时间O(n^2) 空间O(1)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        while True:
            collided = False
            i = 1
            while i < len(asteroids):
                if asteroids[i] < 0 and asteroids[i-1] > 0:
                    if abs(asteroids[i]) > abs(asteroids[i-1]):
                        del asteroids[i-1]
                    elif abs(asteroids[i]) < abs(asteroids[i-1]):
                        del asteroids[i]
                    else:
                        del asteroids[i-1:i+1]
                    collided = True
                else:
                    i += 1
            if not collided:
                break
        return asteroids

    # 栈模拟
    # 时间O(n) 空间O(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True  # 当前asteroid是否没有爆炸
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                alive = -asteroid > stack[-1]
                if -asteroid >= stack[-1]:
                    stack.pop()
            if alive:
                stack.append(asteroid)
        return stack
