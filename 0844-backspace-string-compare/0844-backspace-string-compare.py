class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Time: O(m+n)
        Space: O(m+n)

        Algorithm:
        We just have to store the chars of both the strings in separate stacks and then compare the
        stacks at the end.
        Note: The constant space two pointer solution is more difficult, explore it later.
        """
        s_stack = []
        t_stack = []

        for char in s:
            if char != "#":
                s_stack.append(char)
            elif char == "#" and s_stack:   # for cases where the first char in string is # and stack is empty
                s_stack.pop()
            
        for char in t:
            if char != "#":
                t_stack.append(char)
            elif char == "#" and t_stack:   # for cases where the first char in string is # and stack is empty 
                t_stack.pop()

        return "".join(s_stack) == "".join(t_stack)