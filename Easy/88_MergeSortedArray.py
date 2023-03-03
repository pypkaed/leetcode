def merge(nums1, m, nums2, n):
    if n == 0:
        return nums1
    i = m - 1
    j = n - 1
    curr = m + n - 1
    while j > -1 and i > -1:
        if nums2[j] > nums1[i]:
            nums1[curr] = nums2[j]
            j -= 1
        else:
            nums1[curr] = nums1[i]
            i -= 1
        curr -= 1
    while j > -1:
        nums1[curr] = nums2[j]
        j -= 1
        curr -= 1
    return nums1


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
print(merge([4,5,6,0,0,0], 3, [1,2,3], 3))
print(merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5))
