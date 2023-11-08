func groupAnagrams(strs []string) [][]string {
    hashmap := make(map[[26]int][]string)
    output := make([][]string, 0)

    // Find out the count of chars for each str, store it in hashmap, then bucket each str based on key
    for _, str := range strs {
        // This loop will be constant time since the length of each strs is constant in the entire array
        var key [26]int
        for _, char := range str {    
            key[int(char) - int('a')] += 1
        }
        if arr, ok := hashmap[key]; ok {
            hashmap[key] = append(arr, str)
        } else {
            hashmap[key] = []string{str}
        }
    }

    // Go through the hashmap and add each value in the output slice
    for _, v := range hashmap {
        output = append(output, v)
    }
    return output
}