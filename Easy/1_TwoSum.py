def twoSum(nums, target):
    ht = dict((v, i) for i, v in enumerate(nums))
    for i in range(0, len(nums)):
        if target - nums[i] in ht:
            if i != ht[target - nums[i]]:
                return i, ht[target - nums[i]]
        ht[nums[i]] = i


print(twoSum([1, 4, 6, 4], 10))
