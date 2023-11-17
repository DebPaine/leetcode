type TimeMap struct {
    kvStore map[string][]map[string]int
}

func Constructor() TimeMap {
    return TimeMap{
        kvStore: make(map[string][]map[string]int),
    }
}

func (this *TimeMap) Set(key string, value string, timestamp int)  {
    if _, ok := this.kvStore[key]; !ok{
        this.kvStore[key] = make([]map[string]int, 0)
    }
    this.kvStore[key] = append(this.kvStore[key], map[string]int{value: timestamp})
}

func (this *TimeMap) Get(key string, timestamp int) string {
    kvList := this.kvStore[key]
    l, r := 0, len(kvList)-1
    closestValue := ""

    for l <= r {
        m := r - (r-l)/2

        // This loop will only run one iteration since kvList[m] only has one map
        for storedValue, storedTimestamp := range kvList[m] {
            if storedTimestamp < timestamp {
                closestValue = storedValue
                l = m + 1
            } else if storedTimestamp > timestamp {
                r = m - 1
            } else {
                return storedValue
            }
        }
    }
    return closestValue
}


/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */