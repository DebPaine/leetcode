func topKFrequent(nums []int, k int) []int {
    counts := make(map[int]int)
    buckets := make([][]int, len(nums)+1)
    output := make([]int, 0)

    // Store the count of the numbers occuring in the array
    for _, num := range nums {
        counts[num] += 1
    }
    // Use the count as the index in buckets array and store the numbers
    for num, count := range counts {
        buckets[count] = append(buckets[count], num)
    }
    // Iterate over the buckets in reverse order to get the most frequent k elements 
    for i := len(buckets) - 1; i >= 0; i-- {
        if len(output) < k {
            output = append(output, buckets[i]...) 
        } else {
            break
        }
    }
    return output
}