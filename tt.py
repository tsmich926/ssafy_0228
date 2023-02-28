# def atoi(s):
#     res = 0
#     for n in s:
#         value = ord(n) - ord('0')
#         res = res*10 + value
#     return res
#
# print(atoi('484'))

#2진수를 16진수로 변경
def bintohex(s):
    resd = 0
    for n in s:
        val = int(n)
        resd += resd*2 + val

    #10진수를 16진으로 변경
    if resd < 10:
        return str(resd)
    else:
        return str((resd-10) + ord('A'))


print(bintohex('0111'))

#2진수를 10진수로
def bintohex2(s):
    resd = int(s[0])*8 + int(s[1])*4 + int(s[2])*2 + int(s[3])


