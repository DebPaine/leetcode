class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = [-1]

        for num in arr[::-1][:len(arr)-1]:
            current_max = max(output[-1], num)
            output.append(current_max)
        
        return output[::-1]
