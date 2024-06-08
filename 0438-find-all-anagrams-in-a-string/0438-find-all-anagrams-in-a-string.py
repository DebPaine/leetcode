class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Solution 1: using Counter to count the letters in the sliding window every iteration
        p_count = Counter(p)
        sw_count = Counter(s[:len(p)])
        output = []
        if sw_count == p_count:
            output.append(0)
        l = 0
        for r in range(len(p), len(s)):
            l += 1
            sw_count = Counter(s[l:r+1])
            if sw_count == p_count:
                output.append(l)
        return output

        # Solution 2: add a letter count to sliding window and removing one every iteration
        # p_count = Counter(p)
        # sw_count = Counter(s[:len(p)])
        # output = []
        # if sw_count == p_count:
        #     output.append(0)
        # l = 0
        # for r in range(len(p), len(s)):
        #     sw_count[s[r]] += 1
        #     sw_count[s[l]] -= 1
        #     if sw_count[s[l]] == 0:
        #         del sw_count[s[l]]
        #     l += 1
        #     if sw_count == p_count:
        #         output.append(l)
        # return output