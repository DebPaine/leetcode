class TimeMap:

    def __init__(self):
        self.kv_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_store:
           self. kv_store[key] = []
        self.kv_store.get(key).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        kv_list = self.kv_store.get(key, [])
        l, r = 0, len(kv_list)-1
        closest_value = ""

        """
        We have to find the closest timestamp value to the required timestamp. We can
        do a linear search (Time: O(n)), but a binary search can be applied here since 
        the timestamps will always be in ascending order.

        Linear search:
        for k, v in kv_list:
            if v <= timestamp:
                closest_value = k
        """

        # We have to do binary search on the timestamp part of the tuple
        while l <= r:    
            m = r - (r-l)//2
            if kv_list[m][1] < timestamp:
                closest_value = kv_list[m][0]
                l = m + 1
            elif kv_list[m][1] > timestamp:
                r = m - 1
            else:
                return kv_list[m][0]
        
        return closest_value



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)