def intersect(nums1, nums2):
    count = {}
    res = []
    for num in nums2:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num in nums1:
        if num in count and count[num] > 0:
            res.append(num)
            count[num] -= 1
    return res


print(intersect([1,2,2,1],[2,2]))
print(intersect([4,9,5],[9,4,9,8,4]))
print(intersect([1,2,2,1],[2]))
