# dv = 10 #이진수:1010 16진수:A
# print(dv,bin(dv),hex(dv))
#십진수,이진수,16진수로 출력

#10진수를 2진수로 바꾸기
# def dectobin(value):
#     for j in range(3,-1,-1):
#         r = value & (1<<j)
#         if r != 0:
#             print(1)
#         else:
#             print(0)
# dectobin(10)


#10진수를 2진수로
# def dectobin(value):
#     s= ''
#     for j in range(3,-1,-1):
#         s += '1' if value & (1<<j) else '0'
#     print(s)

#16진수를 10진수로
def hextodec(s):
    #s가 숫자면
    if s.isdigit():
        return int(s)
    else:
        #0 +10
        return ord(s) - ord('A') + 10

print(hextodec('5'))
print(hextodec('B'))

    # s= ''
    # for j in range(3,-1,-1):
    #     s += '1' if value & (1<<j) else '0'
    # print(s)


def hextobin(s):
    #16진수를 10 진수로
    if s.isdigit():
        decv = int(s)
    else:
        decv = ord(s) - ord('A') + 10

    res = ''
    for j in range(3,-1,-1):
        res += '1' if decv & (1<<j) else '0'
    return res

print(hextobin('F'))
print(hextobin('A'))
print(hextobin('5'))


# def hextobin(s):
#     mapping = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000'
#                '9':'1001','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}


'7329'
def atoi(s):
    res = 0
    for n in s:
        value = int(n)
        res *= 10 + value
    return res


def bintodec(s):

#2진수를 16진수로
def bintohex(s):
    res = 0
    for n in s:
        value = int(n)
        res *= 2 + value
    return res