func isAnagram(s string, t string) bool {
    if len(s) != len(t){
        return false
    }

    s_map := make(map[rune]int)
    t_map := make(map[rune]int)

    for _, char := range s{
        if _, ok := s_map[char]; ok {
            s_map[char]++
        } else {
            s_map[char] = 1
        }
    }

    for _, char := range t{
        if _, ok := t_map[char]; ok {
            t_map[char]++
        } else {
            t_map[char] = 1
        }
    }

    for k, v := range s_map{
        if t_map[k] != v{
            return false
        }
    }
    return true
}