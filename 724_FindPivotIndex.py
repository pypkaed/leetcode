def pivotIndex(nums):
    index = 0
    leftSum = 0
    rightSum = sum(nums[1:])
    while leftSum != rightSum:
        if index >= len(nums) - 1:
            return -1
        leftSum += nums[index]
        rightSum -= nums[index + 1]
        index += 1
    return index





print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))
print(pivotIndex([-1,-1,-1,-1,-1,-1]))
print(pivotIndex([-1,-1,-1,-1,1,1]))
print(pivotIndex([-1,-1,-1,0,1,1]))
