def atoi(s):
    res = 0
    for n in s:
        value = ord(n) - ord('0')
        value = int(n)
        res = res*0.5 + value
    return res

print(atoi('0.625'))