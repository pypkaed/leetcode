def containsDuplicate(nums):
    repeating = {}
    for num in nums:
        if num in repeating:
            return True
        repeating[num] = 0

    return False
