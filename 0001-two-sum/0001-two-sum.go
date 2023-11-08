func twoSum(nums []int, target int) []int {
    complement := make(map[int]int)   

    for i, num := range(nums) {
        if val, ok := complement[target - num]; ok {
            return []int{val, i}
        } else {
            complement[num] = i
        }
    }
    return []int{1}
}