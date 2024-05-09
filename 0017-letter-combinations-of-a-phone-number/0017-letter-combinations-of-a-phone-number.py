class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time: O(n*4**n), since worst case we can have is "9999" and each 9 has 4 chars, so 4*4*4*4 = 4*n
        Space: O(n)

        Algorithm:
        Easy problem, we just need to understand the decision tree. Our output char combinations will always have
        the first char from the first digit. The rest of the digits we can find the combinations.
        """
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        output = []

        def backtrack(digits, combination):
            if len(digits) == 0:
                output.append(combination)
                return
            
            for char in mapping[digits[0]]:
                backtrack(digits[1:], combination + char)
        
        if not digits:
            return ""

        backtrack(digits, "")
        return output