from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        sorted_items = sorted(count.items(), key=lambda item: item[1],reverse=True)
        return [num for num, _ in sorted_items[:k]]
