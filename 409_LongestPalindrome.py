def longestPalindrome(s):
    repeating = {}
    longest = 0
    for c in s:
        if c in repeating:
            repeating[c] += 1
        else:
            repeating[c] = 1
    for c in repeating:
        if repeating[c] > 1:
            longest += repeating[c] if repeating[c] % 2 == 0 else repeating[c] - 1
    if longest < len(s): longest += 1
    return longest


print(longestPalindrome("abccccdd"))
print(longestPalindrome("a"))
print(longestPalindrome("bananas"))
