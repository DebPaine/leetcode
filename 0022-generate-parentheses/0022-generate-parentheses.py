class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time: O(2**n), where n is the number of bracket pairs
        Space: O(n), due to a call stack for recursion 
        """
        output = []

        def generate(brackets, open_brackets, closed_brackets):
            if len(brackets) >= 2*n:
                output.append(brackets)
                return
            if closed_brackets < open_brackets:
                generate(brackets + ')', open_brackets, closed_brackets + 1)
            if open_brackets < n:
                generate(brackets + '(', open_brackets + 1, closed_brackets)

        generate('(', 1, 0)
        return output
                

