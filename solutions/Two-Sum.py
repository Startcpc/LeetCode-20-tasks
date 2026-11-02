def twoSum(nums: list[int], target: int) -> list[int]:
    ras = {}
    for i,num in enumerate(nums):
        if num in ras:
            return ras[num],i
        r = target - num
        ras[r] = i
