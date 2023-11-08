func containsDuplicate(nums []int) bool {
    set := make(map[int]bool)
    for _, num := range nums {
        if _, ok := set[num]; ok {
            return true
        } else {
            set[num] = true
        }
    }
    return false
}