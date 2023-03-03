def firstUniqChar(s):
    repeating = {}
    for i in range(len(s)):
        if s[i] in repeating:
            repeating[s[i]] = -1
        else:
            repeating[s[i]] = i
    for c in s:
        if repeating[c] != -1:
            return repeating[c]
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
