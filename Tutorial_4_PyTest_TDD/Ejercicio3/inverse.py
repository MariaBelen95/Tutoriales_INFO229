def inverse(s):
    r = ''
    for i in range(len(s)):
        r+=s[-(i+1)]
    return r
