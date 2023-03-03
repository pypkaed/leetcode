def isAnagram(s, t):
    if len(s) != len(t):
        return False
    pisya = {}
    for c in s:
        if c in pisya:
            pisya[c] += 1
        else:
            pisya[c] = 1
    for c in t:
        if c in pisya:
            pisya[c] -= 1
            if pisya[c] < 0:
                return False
        else:
            return False
    return True
