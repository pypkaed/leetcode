def compress(chars):
    count = 1
    i = -1
    while i < len(chars):
        i += 1
        if i < len(chars) - 1 and chars[i] == chars[i + 1]:
            count += 1
        else:
            if count > 1:
                first = i - count + 1
                for c in str(count):
                    chars[first + 1] = c
                    first += 1
                del (chars[first + 1:i + 1])
                i = first
            count = 1

    return len(chars), chars


print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(compress(["a","a","a","b","b","a","a"]))
print(compress(["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))

