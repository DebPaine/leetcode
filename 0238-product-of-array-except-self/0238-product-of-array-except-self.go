func productExceptSelf(nums []int) []int {
    output := make([]int, len(nums))
    output[0] = 1  // prefix of first element is 1 since there is no element before it

    // Calculate prefix of each element in nums and store it in output
    prefix := 1
    for i, num := range nums[:len(nums)-1] {
        prefix *= num
        output[i+1] = prefix
    }

    // Calculate postfix of each element in nums and multiply it with prefix in output array
    postfix := 1
    for i := len(nums) - 1; i > 0; i-- {
        postfix *= nums[i]
        output[i-1] *= postfix
    }
    return output
}