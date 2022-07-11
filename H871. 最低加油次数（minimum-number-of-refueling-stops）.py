class Solution:
    # 贪心
    # 时间O(nlogn) 空间O(n)
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans, cur, next_station, fuels = 0, startFuel, 0, []
        stations.append([target, 0])
        while cur < target:
            while next_station < len(stations) - 1 and stations[next_station][0] <= cur:
                heappush(fuels, -stations[next_station][1])
                next_station += 1
            while cur < stations[next_station][0] and fuels:
                cur += -heappop(fuels)
                ans += 1
            if cur < stations[next_station][0]:
                return -1
        return ans