def longestCommonPrefix(strs):
    res = ""
    for i in range(0, len(min(strs, key=len))):
        for j in range(0, len(strs) - 1):
            if strs[j][i] != strs[j+1][i]:
                return res
        res += strs[0][i]
    return res


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["racecar", "car", "dog"]))
