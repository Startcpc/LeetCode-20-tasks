class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        see = set()

        for i, num in enumerate(nums):
            if i > k:
                see.remove(nums[i - k - 1])
            if num in see:
                return True
            see.add(num)

        return False
