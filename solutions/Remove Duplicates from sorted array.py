def removeDuplicates(nums: list[int]) -> int:
    k = 0
    f = {}
    for x in nums:
        if x not in f:
            f[x] = k
            nums[k] = x
            k+=1
    return k
