class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1), not counting the output array

        Algorithm:
        We can go through the array in reverse as this will be easier for us to calculate the greatest right
        side element of every element in the array. 
        """

        output = [-1]

        # len(arr)-1 since we have to finish one element before as this will be the current element's greatest right side
        for num in arr[::-1][:len(arr)-1]:  
            current_max = max(output[-1], num)  # since output[-1] will always contain the current max value on the right side
            output.append(current_max)
        
        return output[::-1]
