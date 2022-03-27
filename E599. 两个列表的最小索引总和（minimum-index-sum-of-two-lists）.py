class Solution:
    # 哈希表
    # 时间O(n1+n2) 空间O(n2)
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans, min_index = [], 2000
        dict2 = {name: i for i, name in enumerate(list2)}
        for i, name in enumerate(list1):
            if name in dict2:
                index = i + dict2[name]
                if index < min_index:
                    min_index = index
                    ans = [name]
                elif index == min_index:
                    ans.append(name)
        return ans