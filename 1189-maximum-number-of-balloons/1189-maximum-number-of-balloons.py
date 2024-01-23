class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Time: O(n), where n is len(text) 
        Space: O(n), as we are using Counter to store the char counts

        Steps:
        1. Count the chars in 'balloon'. We have to see min how 
        many letters are needed to form the word 'balloon'
        2. Count the chars in text and store it
        3. Compare count of text with count of 'balloon', use the following:
        text_count[char]//balloon_count[char]
        The above formula should give an integer of how many a particular char in balloon can be used. 
        Eg: text = "loonbalxballpoon", count for letter "l"= 4//2 = 2
        We then keep counting all the letters in text and checking the min count of the letter, this 
        will determine which letter is present the least in text and will tell us that this is
        the min amount of 'balloons' that can be formed using text
        """
        if len(text) < len('balloon'):
            return 0

        balloon_count = Counter('balloon')
        text_count = Counter(text)
        min_count = math.inf

        for char, count in text_count.items():
            # We continue with the next iteration if char is not present in 'balloon' we should not return 0 
            # here as there can be more chars in text which are in 'balloon'
            if char not in balloon_count:
                continue
            min_count = min(min_count, count//balloon_count[char])
        
        return min_count
        
        
