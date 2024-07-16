class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)

        Algorithm:
        We are using bucket sort and storing the nums in different buckets based on their count. We use
        the bucket indices for the count. Once the nums are in appropriate buckets, we then iterate over the
        buckets array in reverse so that we get the most frequent elements first. We then return only the 
        top k elements as per the requirement.
        """
        
        buckets = [[] for _ in range(len(nums) + 1)]
        output = []
        num_count = Counter(nums)

        for num, count in num_count.items():
            buckets[count].append(num)

        for sublist in buckets[::-1]:
            if sublist:
                output += sublist

        return output[:k]
