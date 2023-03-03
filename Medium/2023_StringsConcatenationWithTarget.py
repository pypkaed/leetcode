from collections import Counter


def numOfPairs(nums, target):
    used = Counter()
    res = 0
    for num in nums:
        if target.startswith(num):
            suffix = target[len(num):]
            if suffix in used:
                res += used[suffix]
        if target.endswith(num):
            prefix = target[:len(target) - len(num)]
            if prefix in used:
                res += used[prefix]
        used[num] += 1
    return res


print(numOfPairs(["777","7","77","77"], "7777"))
