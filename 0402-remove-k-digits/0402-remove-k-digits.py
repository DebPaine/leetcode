class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            # digit = int(digit)    # no need to convert to int as we can directly compare the ASCII values of the digits
            while stack and k > 0 and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit) 

        # while k > 0:
        #     stack.pop()
        #     k -= 1

        if k > 0:
            stack = stack[:-k]

        output = "".join(stack).lstrip("0")     # if there is a leading 0 in the beginning
        return output if output else "0"