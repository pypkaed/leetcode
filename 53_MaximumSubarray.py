def maxSubArray(nums):
    cur_sum = 0
    max_sum = nums[0]
    for num in nums:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum

print(maxSubArray([-1, -1, -1, -1]))
