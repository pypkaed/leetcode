def isIsomorphic(s, t):
    repeating = {}
    for i in range(len(s)):
        if s[i] in repeating and repeating[s[i]] != t[i] \
                or t[i] in repeating.values() and s[i] not in repeating:
            return False
        repeating[s[i]] = t[i]

    return True


print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("badc", "baba"))
