from collections import  OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            v = self.dict.pop(key)
            self.dict[key] = v
            return v

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # 这个若是满了，字典第一项是最后加进去的
                self.dict.popitem(last=False)
        self.dict[key] = value
