roman_int = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def isPrefix(f, t):
    if roman_int[f] == 1 and (roman_int[t] == 5 or roman_int[t] == 10):
        return True
    if roman_int[f] == 10 and (roman_int[t] == 50 or roman_int[t] == 100):
        return True
    if roman_int[f] == 100 and (roman_int[t] == 500 or roman_int[t] == 1000):
        return True
    return False


def romanToInt(s):
    res = 0
    for i in range(0, len(s) - 1):
        if isPrefix(s[i], s[i + 1]):
            res -= roman_int[s[i]]
        else:
            res += roman_int[s[i]]
    res += roman_int[s[len(s) - 1]]
    return res

print(romanToInt("MCMXCIV"))
