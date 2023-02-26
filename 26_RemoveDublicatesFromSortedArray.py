def removeDuplicates(nums):
    curr_i = i = 0
    count = len(nums)
    while curr_i < len(nums):
        nums[i] = nums[curr_i]
        curr_i += 1
        while curr_i != len(nums) and nums[curr_i] == nums[i]:
            curr_i += 1
            count -= 1
        i += 1
    return count, nums


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1,1,2]))
