class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            letter_count = [0]*26
            for char in word:
                letter_count[ord(char) - ord("a")] += 1
            anagrams[tuple(letter_count)].append(word)

        return list(anagrams.values())