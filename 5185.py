# def hextobin(s):
#     #16진수를 10 진수로
#     if s.isdigit():
#         decv = int(s)
#     else:
#         decv = ord('s') - ord('A') + 10
#
#     res = ''
#     for j in range(3,len(s)-1,-1):
#         res += '1' if decv & (1<<j) else '0'
#
#     return res
# print(hextobin('47FE'))



    #10진수를 2진수로 변경
#     s= ''
#     for j in range(3,-1,-1):
#         s += '1' if res & (1<<j) else '0'
#     return s
#
#     print(hextobin('47FE'))
#
#
# def hextobin(s):
#     mapping = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000'
#                '9':'1001','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
#
# print(hextobin(47FE))

# def hextobin(s):
#     #16진수를 10 진수로
#
#     if s.isdigit():
#         decv = int(s)
#     else:
#         decv = ord(s) - ord('A') + 10
#
#     res = ''
#     for j in range(2,-1,-1):
#         res += '1' if decv & (1<<j) else '0'
#     return res

#
#
# for i in range(len('FA5')):
#     while i < len(s):

# print(hextobin('FA5'))
# print(hextobin('A'))
# print(hextobin('5'))


def hextobin(s):
    #16진수를 10 진수로
    if s.isdigit():
        decv = int(s)
    else:
        decv = ord('s') - ord('A') + 10

    res = ''
    for j in range(3,-1,-1):
        res += '1' if decv & (1<<j) else '0'

    return res





T = int(input())
for tc in range(1,T+1):
    N,S = input().split()
    num = int(N)
    i = 0
    eq = ''
    while i < len(S):
        eq += hextobin(S[i])
        i += 1
    print(eq)