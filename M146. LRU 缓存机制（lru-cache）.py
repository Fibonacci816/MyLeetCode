class LRUCache:
    # 使用有序字典（也可以使用哈希表 + 双向链表）
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.que = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.que:
            value = self.que.pop(key)
            self.que[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:     
        if key in self.que:
            self.que.pop(key)  
        else:
            if len(self.que) == self.capacity:
                self.que.popitem(last=False)
        self.que[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)