class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        j = set()

        for i in nums:
            if i not in j:
                j.add(i)
            else:
                j.remove(i)
        return j.pop()
