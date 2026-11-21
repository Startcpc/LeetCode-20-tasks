class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        na = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in na]
