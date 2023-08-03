import sys
class LRUCache:

    def __init__(self, capacity: int):
        self.objs = {}
        self.capacity = capacity
        self.curr_cnt = 0

    def get(self, key: int) -> int:
        if key in self.objs:
            self.objs[key][1] = self.curr_cnt
            self.curr_cnt += 1
            return self.objs[key][0]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if not key in self.objs and len(self.objs) == self.capacity:
            min_cnt = sys.maxsize
            old_key = ''
            for obj_key, obj_value in self.objs.items():
                if min_cnt > obj_value[1]:
                    old_key = obj_key
                    min_cnt = obj_value[1]
            self.objs.pop(old_key)
        self.objs[key] = [value, self.curr_cnt]
        self.curr_cnt += 1
