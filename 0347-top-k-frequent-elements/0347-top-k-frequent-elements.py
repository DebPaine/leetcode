class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        output = []
        num_count = Counter(nums)

        for num, count in num_count.items():
            buckets[count].append(num)

        for sublist in buckets[::-1]:
            if sublist:
                output += sublist

        return output[:k]
