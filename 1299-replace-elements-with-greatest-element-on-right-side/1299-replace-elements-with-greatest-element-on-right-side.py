class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Time: O(n), where n is len(arr)
        Space: O(1), if we are not counting output array

        Instead of iterating from start to finish and comparing the elements to it's
        right, we can go in reverse and only calculate it's next element. 
        """
        current_max = -math.inf
        output = [-1]

        for i in range(len(arr)-2, -1, -1):
            current_max = max(current_max, arr[i+1])
            output.append(current_max) 

        return output[::-1]