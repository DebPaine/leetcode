class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(m*n), where m is the len(strs) and n is the len(individual words)
        Space: O(m)

        Algorithm:
        We have to group the words together based on their letter counts. We can use an array
        of ascii values of letters to group the words. We can then store the letter counts as 
        a key in a dictionary and append all the words which have the same letter count. 
        
        Note: We convert letter_count to tuple as we can't have a list as a dict key. 
        """
        
        anagrams = defaultdict(list)

        for word in strs:
            letter_count = [0]*26   # O(26) space
            for char in word:
                letter_count[ord(char) - ord("a")] += 1
            anagrams[tuple(letter_count)].append(word)

        return list(anagrams.values())